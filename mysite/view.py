from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world")

def home(request):
    return render(request, 'mysite/index.html')
    # return render(request, 'template/index.html')

def test(request):
    return render(request, 'mysite/test.html')