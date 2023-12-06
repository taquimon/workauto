from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def apiauto(request):
    template = loader.get_template('first.html')
    return HttpResponse(template.render())


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def all(request):
    template = loader.get_template('all.html')
    return HttpResponse(template.render())
# Create your views here.
