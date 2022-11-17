from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from women.models import *

menu = ["О сайте","Добавить статью", "Обратная свзяь","Войти"]

def index(request):
    posts = Women.objects.all()
    
    return render(request,'women/index.html',{'posts':posts,'menu':menu,'title':'Главная страница'})

def about(request):
    return render(request,'women/about.html',{'menu':menu,'title':' О сайте'})

def categories(request,catid):
    if(request.GET):
        print(request.GET)
    return HttpResponse(f"<h1> Статься по категориям</h1> <p>{catid}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена</h1>')