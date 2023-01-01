from django.shortcuts import render
# from django.http import HttpResponse

from pronunciar_dni_app.api import pronunciar_dni

def home(request):
    return render(request, "index.html")

def about(request):
    return render (request, "About.html")

def contact (request):
    return render (request, "Contact.html")

def result_page (request, dni):
    dni = int (dni)
    resultados = pronunciar_dni.GET_BESTS_PATTERNS(dni, 3)
    return render(
        request, 'result.html',
        {
            'results': resultados,
        }
    )

