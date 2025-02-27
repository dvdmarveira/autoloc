from django.shortcuts import render
from django.http import FileResponse, HttpResponse
import os
from django.conf import settings

def baixar_zip(request):
    caminho_zip = os.path.join(settings.MEDIA_ROOT, 'downloads', 'dist.zip')

    if os.path.exists(caminho_zip):
        return FileResponse(open(caminho_zip, 'rb'), as_attachment=True, filename="dist.zip")
    else:
        return HttpResponse("Arquivo não encontrado", status=404)

def index(request):
    return render(request, 'index.html')
