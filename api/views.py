from django.shortcuts import render, redirect
from django.http import HttpResponse

def main(request):
    return HttpResponse('<h1>Screw me/<h1>')
