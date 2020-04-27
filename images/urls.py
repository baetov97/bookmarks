from django.urls import path
from .views import *
urlpatterns = [
    path('create/', image_create, name='create'),
]
