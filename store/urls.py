from django.urls import path

from .views import *


urlpatterns = [
    path("", ApiView.as_view()),
    path("api/<int:pk>/", SingleApiView.as_view()),
]