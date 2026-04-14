

from django.contrib import admin
from django.urls import include, path
from constructions import views
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
]