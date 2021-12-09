from django.shortcuts import render
from .models import Resume


def homepage(request):
    cv = Resume.objects.all()
    return render(request,'homepage/homepage.html',{'cv':cv})

# Create your views here.

