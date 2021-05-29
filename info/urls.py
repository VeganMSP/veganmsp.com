from django.urls import path

from . import views

urlpatterns = [
	path('restaurants/', views.restaurants, name='restaurants'),
]
