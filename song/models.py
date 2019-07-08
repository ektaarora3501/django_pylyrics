from django.db import models
from django.urls import reverse

# Create your models here.

class Regis(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    user_name=models.CharField('Dude Name',max_length=100,unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=12)
    #cnf_pass=models.CharField(max_length=12)

    def __str__(self):
        return f'{self.user_name},{self.email}'

#    def get_absolute_url(self):
#        return reverse('profile-detail',args=[(self.user_name)])
