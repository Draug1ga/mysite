from django.urls import path
from . import views


app_name = 'aboutme'

urlpatterns = [
    path('contact/', views.aboutme, name='aboutme')
]

