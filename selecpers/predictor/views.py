from django.shortcuts import render, redirect
from .forms import CandidatoForm
from .models import Candidato
import numpy as np
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import load_model
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image
from reportlab.lib.styles import ParagraphStyle
import matplotlib.pyplot as plt
from io import BytesIO
import base64

modelo = load_model('predictor/modelo/select_candidate.h5')



# Importa las bibliotecas necesarias
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from django.shortcuts import render
from .models import Candidato

# Define la función de la vista
def estadisticas(request):
    # Obtén las estadísticas de categorías
    estadisticas = {
        'Regular': Candidato.objects.filter(candidato=1).count(),
        'Bueno': Candidato.objects.filter(candidato=2).count(),
        'Muy Bueno': Candidato.objects.filter(candidato=3).count(),
    }

    # Genera el gráfico de barras
    plt.bar(estadisticas.keys(), estadisticas.values())
    plt.xlabel('Categoría')
    plt.ylabel('Número de Candidatos')
    plt.title('Estadísticas de Categorías')

    # Guarda el gráfico en un objeto BytesIO y conviértelo a base64
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    grafico_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    plt.close()

    # Renderiza la plantilla HTML con las estadísticas y el gráfico
    return render(request, 'predictor/estadisticas.html', {'estadisticas': estadisticas, 'grafico_base64': grafico_base64})



def generar_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="candidatos.pdf"'

    # Obtener todos los candidatos de la base de datos
    candidatos = Candidato.objects.all()

    # Crear un documento PDF
    pdf = SimpleDocTemplate(response, pagesize=letter)
    elementos = []

    # Definir estilos para el título y el subtítulo
    estilo_titulo = ParagraphStyle(name='Title', fontSize=20, alignment=1, spaceAfter=12)
    estilo_subtitulo = ParagraphStyle(name='Subtitle', fontSize=16, alignment=1, spaceAfter=12)

    # Agregar el título y el subtítulo al documento
    elementos.append(Paragraph('<b>HR-SIL Predicciones</b>', estilo_titulo))
    elementos.append(Paragraph('<br/><br/>'))  # Agregar espacio en blanco
    elementos.append(Paragraph('<b>Resultados Predicciones</b>', estilo_subtitulo))
    elementos.append(Paragraph('<br/><br/>'))  # Agregar espacio en blanco

    # Agregar tabla de datos
    tabla_datos = []

    # Agregar encabezados a la tabla
    encabezados = ['Nombre', 'Experiencia', 'Idioma', 'VE', 'FYS', 'Candidato']
    tabla_datos.append(encabezados)

    # Agregar datos de los candidatos a la tabla
    for candidato in candidatos:
        fila = [candidato.name, candidato.experiencia, candidato.idioma, candidato.ve, candidato.fys, candidato.candidato]
        tabla_datos.append(fila)

    # Crear la tabla PDF
    tabla = Table(tabla_datos)

    # Estilo de la tabla
    estilo_tabla = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    tabla.setStyle(estilo_tabla)

    # Agregar tabla al documento
    elementos.append(tabla)

    # Generar gráfico de torta
    categorias = ['Regular', 'Bueno', 'Muy Bueno']
    conteos = [candidatos.filter(candidato=i).count() for i in range(1, 4)]

    plt.figure(figsize=(6, 6))
    plt.pie(conteos, labels=categorias, autopct='%1.1f%%')
    plt.title('Distribución de categorías')
    plt.axis('equal')  # Hacer que el gráfico sea circular

    # Guardar el gráfico en un objeto BytesIO
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()

    # Convertir el objeto BytesIO a base64 para incrustarlo en el PDF
    grafico_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    imagen_grafico = Image(BytesIO(base64.b64decode(grafico_base64)), width=300, height=300)
    elementos.append(imagen_grafico)

    # Construir el documento PDF
    pdf.build(elementos)

    return response





def borrar_candidatos(request):
    if request.method == 'POST':
        Candidato.objects.all().delete()
    return redirect('predecir_candidato')

def switch_case(argument):
    match argument:
        case 1:
            return "Regular"
        case 2:
            return "Bueno"
        case 3:
            return "Muy Bueno"
        case _:
            return "Default case"

def predecir_candidato(request):
    form = CandidatoForm()

    if request.method == 'POST':
        form = CandidatoForm(request.POST)
        if form.is_valid():
            # Obtener datos del formulario
            nuevo_candidato = np.array([[int(form.cleaned_data['experiencia']),
                                         int(form.cleaned_data['idioma']),
                                         int(form.cleaned_data['ve']),
                                         int(form.cleaned_data['fys'])]]).reshape(1, -1)

            # Realizar predicciones en datos estandarizados
            probabilidades = modelo.predict(nuevo_candidato)[0]
            clase_predicha = np.argmax(probabilidades) + 1

            # Crear un nuevo objeto Candidato y guardarlo en la base de datos
            candidato = Candidato(
                name=form.cleaned_data['name'],
                experiencia=form.cleaned_data['experiencia'],
                idioma=form.cleaned_data['idioma'],
                ve=form.cleaned_data['ve'],
                fys=form.cleaned_data['fys'],
                candidato=clase_predicha
            )
            candidato.save()

            # Obtener la clase predicha en texto
            result = switch_case(clase_predicha)
            # Recuperar todos los candidatos almacenados en la base de datos
            candidatos = Candidato.objects.all()
            return render(request, 'predictor/resultado.html', {'clase_predicha': result, 'nuevo_candidato': nuevo_candidato, 'name_candidato': form.cleaned_data['name'], 'candidatos': candidatos})
            
    return render(request, 'predictor/formulario.html', {'form': form})
