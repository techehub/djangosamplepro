from django.db import models

# Create your models here.



class Student (models.Model):
    rollNo = models.CharField(max_length=50)
    name = models.CharField (max_length=100)
    mark = models.IntegerField(default=0)
    email= models.EmailField(max_length=50)
    phone = models.CharField(max_length=10)
    status= models.CharField(max_length=1, default="P")

    def __str__(self):
        return self.rollNo + " :" + self.name


class Contact (models.Model) :
    name  = models.CharField(max_length=100)
    phone = models.CharField( max_length=100)
    email = models.EmailField( max_length=100)
    message = models.CharField( max_length=250)

    def __str__(self):
        return self.name + " :" + self.email