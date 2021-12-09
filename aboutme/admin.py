from django.contrib import admin
from . models import Work, Messageme

# Register your models here.
admin.site.register(Work),
admin.site.register(Messageme)


#python manage.py create superuser