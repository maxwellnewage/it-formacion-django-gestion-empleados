from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about_us, name="about-us"),
]
