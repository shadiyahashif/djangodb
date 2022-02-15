from django.db import models

# Create your models here.

class Member(models.Model):
     f_name = models.CharField(max_length=30)
     l_name = models.CharField(max_length=30)
     email = models.EmailField(max_length=200)
     password = models.CharField(max_length=100)
     age = models.IntegerField()

     def __str__(self):
         return self.f_name +" "+self.l_name