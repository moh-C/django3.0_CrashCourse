from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'index.html', {'name': 'Lardass'})


def result(request):
    res = int(request.POST['num1']) + int(request.POST['num2'])
    return render(request, 'result.html', {'result': res})
