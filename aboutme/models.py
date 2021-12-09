from django.db import models

# Create your models here.
class Work(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    # add in thumbnail later

class Messageme(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email_address = models.EmailField()
    message = models.TextField (max_length = 1000)


    def __str__(self):
        return self.first_name