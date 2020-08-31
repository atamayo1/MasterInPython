from django.shortcuts import render


# Create your views here.
def index(request):
    title='Home'
    year=2020
    hasta=2040
    titleYears=f'Años hasta el {str(hasta)}'
    years=range(year,hasta)
    return render(request, 'mainapp/index.html', {
        'title': title,
        'titleYears': titleYears,
        'years': years
    })


def about(request):
    title='Sobre nosotros'
    content='Soy Anthony Tamayo Ortega , desarrollador web'
    codes=['JavaScript', 'Python', 'Java', 'PHP']
    year=2020
    hasta=2040
    titleYears=f'Años hasta el {str(hasta)}'
    years=range(year,hasta)
    return render(request, 'mainapp/about.html', {
        'title': title,
        'content': content,
        'codes':codes,
        'titleYears':titleYears,
        'years':years
    })
