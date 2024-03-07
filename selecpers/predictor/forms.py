from django import forms
OPCIONES_BINARIAS = [(1, 'Demuestra'), (0, 'No demuestra')]

OPCIONES_EXPERIENCIA = [(0, 'No tiene experiencia'),
                        (2, 'Menos de un año'),
                        (6, 'Mas de un año'),
                        (8, 'Mas de 3 años'),
                        (10, 'Mas de 5 años')]

OPCIONES_IDIOMA = [(0, 'No sabe ingles'),
                   (2, 'Puedo expresarme y entiendo'),
                   (5, 'First Certificate /TOEFL / Advance'),
                   (10, 'Proficiency')]

class CandidatoForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    experiencia = forms.ChoiceField(label='Experiencia',choices=OPCIONES_EXPERIENCIA, widget=forms.Select(attrs={'class': 'form-select'}))

    idioma = forms.ChoiceField(label='Idioma', choices=OPCIONES_IDIOMA, widget=forms.Select(attrs={'class': 'form-select'}))

    ve = forms.ChoiceField(label='Voluntad Entusiasta', choices=OPCIONES_BINARIAS, widget=forms.Select(attrs={'class': 'form-select'}))

    fys = forms.ChoiceField(label='Firmeza y Seguridad', choices=OPCIONES_BINARIAS, widget=forms.Select(attrs={'class': 'form-select'}))
