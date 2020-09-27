from django.urls import path
from . import views


urlpatterns = [
    path('doctors/', views.doctors, name="doctors"),
    path('appointment/<str:list_id>/', views.appointment, name="appointment"),

]
