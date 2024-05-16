from django.shortcuts import render
from django.http import HttpResponse
import os

# current_dir = os.path.dirname(__file__)
# model_path = os.path.join(current_dir, 'models/classification_model.h5')
# model = load_model(model_path)

def dashboard(request):
    return render(request, 'dashboard.html')

def prediksi(request):
    return render(request, 'prediksi.html')

def customerjourneymap(request):
    return render(request, 'cjm.html')

def customerjourneymap_graph(request):
    return render(request, 'components/cjm_chart.html')

def analisa(request):
    return render(request, 'analisa.html')

