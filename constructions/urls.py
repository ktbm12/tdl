from django import path, views


urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
]