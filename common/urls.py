"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import homepage, mypage1, mypage2, resultpage, \
    studentinfo,contactpage, signuppage,logoutpage, loginpage

from django.conf.urls import include



urlpatterns = [
    path('home', homepage),
    path('abc', mypage1),
    path('xyx', mypage2),
    path ('result', resultpage),
    path ('sinfo', studentinfo),
    path ('contact', contactpage),
    path ('signup', signuppage),
    path ('logout', logoutpage),
    path ('login', loginpage),
    #path('accounts/', include('django.contrib.auth.urls')),


]
