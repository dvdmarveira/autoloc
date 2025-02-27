from django.urls import path
from .views import index, baixar_zip

urlpatterns = [
    path('',index, name='index'),
    path('download-zip/', baixar_zip, name='download_zip'),
]
