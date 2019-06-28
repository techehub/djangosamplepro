from django.contrib import admin
from .models import Student, Contact
from django.contrib.auth.forms import UserCreationForm
# Register your models here.

admin.site.register(Student)
admin.site.register(Contact)

