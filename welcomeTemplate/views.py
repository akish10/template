from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
template=loader.get_template('index.html')
def template1(request):
    return HttpResponse(template.render())
