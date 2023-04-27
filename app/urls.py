from django.urls import path
from app import views
from .api import PersonViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('api/person', PersonViewSet, 'person')

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about_us, name="about-us"),
    path('person/delete/<str:person_id>', views.delete_person, name="person-delete"),
    path('person/create', views.create_person, name="person-create"),
    path('person/update/<str:person_id>', views.update_person, name="person-update"),
    path('employee/delete/<str:employee_id>', views.delete_employee, name='employee-delete'),
    path('employee/create/', views.create_employee, name="employee-create"),
] + router.urls
