from django.urls import path
from . import views

# Trailing slash is important, wont work without it in safari
# Order of the paths is also important
#
urlpatterns = [
    path("", views.home),
    path("aboutme/", views.index),
    # path("january/", views.january),
    # path("february/", views.february),
    path("<int:month>", views.monthly_challenge_with_month_as_digit),
    path("<str:month>", views.monthly_challenge),
    path("<fname>/<lname>", views.say_hello)
]