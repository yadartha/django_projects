from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home,name="home"),
    path('', views.index,name="index"),
    path('login', views.loginUser,name="login"),
    path('register', views.registerUser ,name="register"),

]