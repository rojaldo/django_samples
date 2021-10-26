import datetime
import json
from django.http.response import JsonResponse
from django.shortcuts import render
from django.core import serializers

from django.http import HttpResponse, HttpResponseRedirect
from samples.calculator_engine import processString
from samples.forms import ContactForm
from samples.models import Customer, Hero, Post, Product
from samples.process import json_to_nasa_APOD, get_beers, get_unsaved_beers
from django.views.generic import CreateView

def hello_world(request):
    name = request.GET.get('name', 'World')
    return HttpResponse('Hello {}!'.format(name))

def getResult(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2
    else:
        return 'Invalid operator'

def calculator(request):
    number_1 = request.GET.get('num1', 0)
    number_2 = request.GET.get('num2', 0)
    operator = request.GET.get('op', '')
    result = getResult(int(number_1), int(number_2), operator)
    return HttpResponse('Operation: ' + number_1 + operator + number_2 + '=' + str(result))

class Athlete:
    def __init__(self, name, age, team):
        self.name = name
        self.age = age
        self.team = team

def hello(request):
    athletes = []
    athletes.append(Athlete('Michael Phelps', 29, 'Swimming'))
    athletes.append(Athlete('Usain Bolt', 28, 'Running'))
    athletes.append(Athlete('Lochte, Martina', 27, 'Swimming'))
    athletes.append(Athlete('Ledecky, Michael', 26, 'Cycling'))

    context = {}
    context['hello'] = '<b>Hi World!</b>'
    context['title'] = 'Mi lista'
    context['athlete_list'] = athletes

    return render(request, 'hello.html', context)


def calculate(request):
    context = {}
    if request.method == "POST":
        content = request.POST
        print(content['expression'])
        stringExpression = content['expression']
        result = processString(stringExpression)
        context['feedback'] = stringExpression + '=' + str(result)
    if request.method == "GET":
        context['feedback'] = 'No expression'
    return render(request, 'sample.html', context)

def show_static_demo(request):
    context = {}
    return render(request, 'static.html', context)

def show_model_demo(request):
    context = {}
    context['customers'] = Customer.objects.all()
    return render(request, 'model.html', context)

def create_model_demo(request):
    name = request.GET.get('name', 'World')
    Customer.objects.create(name='Customer 1', age=19)
    return HttpResponse('Customer created! {}'.format(Customer.objects.last()))

def heroes(request):
    context = {}
    if request.method == "POST":
        content = request.POST
        heroName = content['name']
        heroDescription = content['description']
        print(content['name'])
        print(content['description'])
        Hero.objects.create(name=heroName, description=heroDescription)
        context['heroes'] = Hero.objects.all()
    if request.method == "GET":
        context['heroes'] = Hero.objects.all()
    return render(request, 'heroes.html', context)

def apod(request):
    #get current date yyyy-mm-dd
    context = {}
    context['nasa'] = json_to_nasa_APOD()
    return render(request, 'apod.html', context)    

def apod_api(request):
    #get current date yyyy-mm-dd
    today = datetime.date.today()
    today = today.strftime('%Y-%m-%d')
    my_date = request.GET.get('date', today)
    apod = json_to_nasa_APOD(my_date)
    return JsonResponse(apod, safe=False)

def beers_api(request):
    beers = serializers.serialize('json', get_beers())
    beers = json.loads(beers)
    my_beers = []
    for beer in beers:
        my_beers.append(beer['fields'])
    return JsonResponse(my_beers, safe=False)

def beers(request):
    #get current date yyyy-mm-dd
    context = {}
    context['beers'] = get_beers()
    return render(request, 'beers.html', context)  

def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Post.objects.create(
                name=cd['name'],
                email=cd['email'],
                message=cd['message']
            )
            # assert False
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request,
        'contact.html',
        {'form': form, 'submitted': submitted})

class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'price')
    template_name = 'product.html'

    def get_success_url(self):
        return '/success/'
    
    def form_valid(self, form):
        form.save()
        print(form.cleaned_data)
        return super().form_valid(form)

def success_view(request):
    context = {}
    return render(request, 'success.html', context)

    
     
    
