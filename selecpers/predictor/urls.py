from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
  path('', views.predecir_candidato, name=''),
  path('borrar_candidatos/', views.borrar_todos_candidatos, name='borrar_candidatos'),
  path('generar_pdf/', views.generar_pdf, name='generar_pdf'),
  path('estadisticas/', views.generar_pdf, name='estadisticas'),
  # Otras URLs de tu aplicación
]

if settings.DEBUG:
  from django.conf.urls.static import static
  urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)