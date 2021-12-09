from django.urls import path, include
from . import views



urlpatterns = [
    path('georgedraughn/', views.homepage, name='homepage'),
    path('georgedraughn/',include('portfolio.urls')),
    path('georgedraughn/',include('aboutme.urls')),
]