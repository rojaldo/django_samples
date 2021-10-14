from django.shortcuts import render

from django.http import HttpResponse
 
def hello_world(request):
    name = request.GET.get('name', 'World')
    return HttpResponse('Hello {}!'.format(name))
