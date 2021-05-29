from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Restaurant

def index(request):
	return HttpResponse("Hello, world. You're at the info index.")


def restaurants(request):
	restaurant_list = Restaurant.objects.order_by('name')
	template = loader.get_template('info/restaurants.html')
	context = {
		'restaurant_list': restaurant_list,
	}
	return HttpResponse(template.render(context, request))
