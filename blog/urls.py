from django.urls import path
from . import views

urlpatterns = [path('blogPage/', views.Blog),
path('words/', views.Words)]
