from urllib.request import Request

from django.shortcuts import render
from .models import Review

MENU = {"Главная": "/", "О блоге": "/about", "Отзывы": "/reviews"}

def reviews_page(request):
    reviews = Review.objects.all()
    title = "Отзывы о блоге | Блог о фильмах и сериалах"
    data = {"menu":MENU, "title":title, "reviews":reviews}
    return render(request, "./reviews.html", context=data)

def thanks_page(request):
    user_name = request.POST['user_name']
    user_mail = request.POST['user_mail']
    user_comment = request.POST['user_comment']
    Review.objects.create(full_name=user_name, email=user_mail, text=user_comment)
    title = "Спасибо за ваш отзыв | Блог о фильмах и сериалах"
    data = {"menu":MENU, "title":title}
    return render(request, "./thanks.html", context=data)