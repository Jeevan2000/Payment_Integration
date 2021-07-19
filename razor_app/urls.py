from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('donate',views.donate,name="donate"),
    path('success',views.success,name="success"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),

]