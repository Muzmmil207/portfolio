from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_portfolio, name="my_portfolio"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('services/', views.services, name="services"),
    path('single_project/', views.single_project, name="single_project"),

]
