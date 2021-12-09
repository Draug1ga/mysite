from django.shortcuts import render,redirect
from .models import Work
from . import forms

def aboutme(request):
    if request.method == 'POST':
        form = forms.MessagemeForm(request.POST)
        form.save()
        return redirect('aboutme:aboutme')
    else:
       works = Work.objects.all()
       form = forms.MessagemeForm()
    return render(request,'aboutme/aboutme.html',{'stuff': works,'message': form})
# Create your views here.