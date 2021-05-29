from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Restaurant


class IndexView(TemplateView):
	template_name = 'info/index.html'


class AboutView(TemplateView):
	template_name = 'info/about.html'


def about(request):
	return HttpResponse("You're at the about page")


def links(request):
	return HttpResponse("You're at the Links List")


def restaurants(request):
	restaurant_list = Restaurant.objects.order_by('name')
	template = loader.get_template('info/restaurants.html')
	context = {
		'restaurant_list': restaurant_list,
	}
	return HttpResponse(template.render(context, request))


def shopping(request):
	return HttpResponse("You're at the Shopping List")
