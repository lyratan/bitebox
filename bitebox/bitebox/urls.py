"""
URL configuration for bitebox project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from django.http import HttpResponse
from django.shortcuts import render

#this is a view function
def  index(request):
    return HttpResponse('<h1>bITEbox</h1> <p> Yum Yum Yummy</p>')

def contactus(request):
    body = ''' <h1>bITEbox</h1>
<p> Yum Yum Yummy</p>
<h2> Contact Us</h2>
<p> You can reach us at inquiry@bitebox.com</p>'''
    return HttpResponse(body)

def login(request):
    return render(request,'webkiosk/login.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('contact/', contactus),
    path('webkiosk/', include('webkiosk.urls')), #webkiosk.urls was added
    path('login/', login)
    
]
