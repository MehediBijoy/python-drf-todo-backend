from django.urls import path

from .views import loginAPI, registerAPI

urlpatterns = [
    path('login/', loginAPI.as_view()),
    path('register/', registerAPI.as_view())
]