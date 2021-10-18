from django.shortcuts import render

from django.http import HttpResponse
from samples.calculator_engine import processString

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
