from django.urls import path
from . import views
from pages.api import PageApi

urlpatterns = [
    path('page/<str:slug>', views.page, name="page"),
    path('api/create_page', PageApi.as_view(), name="api_create_page")
]