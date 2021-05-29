from django.urls import path

from . import views

app_name = 'info'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('about/', views.AboutView.as_view(), name='about'),
	path('links/', views.LinkIndex.as_view(), name='links'),
	path('restaurants/', views.RestaurantIndex.as_view(), name='restaurants'),
	path('shopping/', views.ShoppingIndex.as_view(), name='shopping'),
]
