from tkinter.font import names

from django.urls import path
from .views import *

urlpatterns = [
    path('', reviews_page),
    path('thanks/', thanks_page, name='thanks_page'),
]