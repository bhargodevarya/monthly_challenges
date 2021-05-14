from django.urls import path
from . import views

urlpatterns = [
    path("aboutme/", views.index),
    path("january/", views.january),
    path("february/", views.february),
    path("<fname>/<lname>", views.say_hello)
]