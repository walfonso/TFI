"""
URL configuration for selecpers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from core import views as core_views
from predictor import views as predictor_views


from django.conf import settings

urlpatterns = [
    path('', core_views.home, name="home"),
    path('predecir_candidato/', predictor_views.predecir_candidato, name="predecir_candidato"),
    path('borrar_candidatos/', predictor_views.borrar_candidatos, name='borrar_candidatos'),
    path('generar_pdf/', predictor_views.generar_pdf, name='generar_pdf'),
    path('estadisticas/', predictor_views.estadisticas, name='estadisticas'),
    path('about-me/', core_views.about, name="about"),
    path('rse/', core_views.rse, name="rse"),
    path('admin/', admin.site.urls),
] 

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)