from django.urls import path
from .views import *
app_name = "authapp"

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('register',UserM.as_view(),name='register'),
    path("user",fileopener,name="userprofile")
]