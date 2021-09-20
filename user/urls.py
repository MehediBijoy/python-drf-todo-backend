from django.urls import path

from .views import loginAPI, registerAPI, userAPI

urlpatterns = [
    path('login/', loginAPI.as_view()),
    path('register/', registerAPI.as_view()),
    path('user_info/', userAPI.as_view())
]