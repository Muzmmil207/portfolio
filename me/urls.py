from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_portfolio, name="my_portfolio"),
    path('about-me/', views.about, name="about"),
    path('contact-me/', views.contact, name="contact"),
    path('my-services/', views.services, name="services"),
    path('single-project/<slug:slug>/', views.single_project, name="single_project"),

]
