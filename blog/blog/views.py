from django.http import HttpResponse
from django.shortcuts import render

MENU = {"Главная": "/", "О блоге": "/about"}
POSTS = {"Достать ножи": "/knives_out"}

def main_page(request):
    title = "Кадр за кадром | Блог о фильмах и сериалах"
    data = {"menu":MENU, "title":title, "posts":POSTS}
    return render(request, "./index.html", context=data)

def about(request):
    title = "О блоге | Кадр за кадром"
    data = {"menu":MENU, "title":title}
    return render(request, "./about.html", context=data)

def knives_out(request):
    title = "Достать ножи | Кадр за кадром"
    data = {"menu":MENU, "title":title}
    return render(request, "./knives_out.html", context=data)