from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Restaurant


class IndexView(TemplateView):
	template_name = 'info/index.html'


class AboutView(TemplateView):
	template_name = 'info/about.html'


class LinkIndex(TemplateView):
	template_name = 'info/links.html'


class RestaurantIndex(ListView):
	template_name = 'info/restaurants.html'

	def get_queryset(self):
		return Restaurant.objects.order_by('name')


class ShoppingIndex(TemplateView):
	template_name = 'info/shopping.html'
