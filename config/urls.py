"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from samples.views import ProductCreateView, hello_world, calculator, calculate, show_static_demo, show_model_demo, create_model_demo, heroes, apod, beers, contact, success_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world),
    path('staticdemo/', show_static_demo),
    path('modeldemo/', show_model_demo),
    path('createcustomer/', create_model_demo),
    path('calculadora/', calculator),
    path('calc/', calculate),
    path('heroes/', heroes),
    path('apod/', apod),
    path('beers/', beers),
    path('contact/', contact),
    path('crispy/', ProductCreateView.as_view()),
    path('success/', success_view)
]
