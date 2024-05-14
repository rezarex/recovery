from django.shortcuts import render
from django.http import JsonResponse
from .forms import RecoveryForm
import requests

NODE_BACKEND_URL = "http://localhost:3001"


def index(request):
    form = RecoveryForm()
    return render(request, 'index.html', {'form': form})


def scan(request):
    if request.method == "POST":
        form = RecoveryForm(request.POST)
        if form.is_valid():
            device = form.cleaned_data['device']
            file_type = form.cleaned_data['file_type']
            response = requests.post(f"{NODE_BACKEND_URL}/scan",
                                     json={'device': device.name, 'file_type': file_type.name})
            recoverable_files = response.json()
            return render(request, 'results.html', {'files': recoverable_files})
    return JsonResponse({'error': 'Invalid request'}, status=400)


def recover(request):
    if request.method == "POST":
        files = request.POST.getlist('files')
        response = requests.post(f"{NODE_BACKEND_URL}/recover", json={'files': files})
        recovered_files = response.json()['recovered_files']
        return JsonResponse({'recovered_files': recovered_files})
    return JsonResponse({'error': 'Invalid request'}, status=400)
