from django.urls import path

from . import views

app_name = 'info'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('about/', views.AboutView.as_view(), name='about'),
	path('links/', views.links, name='links'),
	path('restaurants/', views.restaurants, name='restaurants'),
	path('shopping/', views.shopping, name='shopping'),
]
