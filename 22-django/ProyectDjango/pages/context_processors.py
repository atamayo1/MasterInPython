from .models import Page

def get_pages(request):
    pages = Page.objects.filter(visible=True).order_by('orden').values_list('id', 'title', 'slug')
    return {
        'pages':pages
    }