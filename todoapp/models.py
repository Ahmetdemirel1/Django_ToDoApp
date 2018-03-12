from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserRegister(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)



class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=52, verbose_name='Baslik')
    description = models.TextField(verbose_name='Aciklama')
    published_date = models.DateTimeField(auto_now_add=True, blank=True)
