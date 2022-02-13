from cgitb import text
from datetime import date, datetime
from email.mime import image
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


# Create your models here.
fs = FileSystemStorage(location='blogposts\media\photos')

class Blogpost(models.Model):
    
    class Language(models.TextChoices):
        PL = 'PL', _('Polski')
        EN = 'EN', _('English')
        DE = 'DE', _('Deutsch')

    title                   =   models.CharField(max_length=100, blank=False)
    text                    =   models.TextField(max_length=5000, blank=False)
    image                   =   models.ImageField(storage = fs)
    date_of_publication     =   models.DateField(blank=True, null=True)
    date_of_create          =   models.DateTimeField(auto_now_add=True)
    language                =   models.CharField(max_length=2, choices=Language.choices, default=Language.PL)
    
    def get_absolute_url(self):
        return reverse('blogposts:blogpost-detail', kwargs={'id': self.id}) #f'/show/{self.id}/'
        
