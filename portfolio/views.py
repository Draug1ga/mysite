from django.shortcuts import render
from .models import Project


def portfolio(request):
    work = Project.objects.all()
    return render(request, 'portfolio/portfolio.html', {'work':work})



    # Create your views here.
