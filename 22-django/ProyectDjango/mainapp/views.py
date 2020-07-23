from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html', {
        'title': 'Bienvenido a la primera pagina',
        'content': 'Año hasta el 2050'
    })


def about(request):
    return render(request, 'mainapp/about.html', {
        'title': 'Sobre nosotros',
        'content': 'Soy Anthony Tamayo Ortega , desarrollador web'
    })
