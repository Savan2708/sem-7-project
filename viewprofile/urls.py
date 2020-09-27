from django.urls import path
from . import views

urlpatterns = [
                  path('viewprofile', views.viewprofile, name="viewprofile"),
              ]
