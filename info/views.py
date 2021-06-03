from django.views.generic import TemplateView, ListView

from blog.models import Post

from .models import (
	FarmersMarket,
	Link,
	Restaurant,
	VeganCompany,
)


class IndexView(TemplateView):
	template_name = 'info/index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['recent_posts_list'] = Post.objects.order_by('-date_created')[:5]
		return context


class AboutView(TemplateView):
	template_name = 'info/about.html'


class LinkIndex(TemplateView):
	template_name = 'info/links.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['links_list'] = Link.objects.order_by('category__name', 'name')
		return context


class RestaurantIndex(ListView):
	template_name = 'info/restaurants.html'

	def get_queryset(self):
		return Restaurant.objects.order_by('name')


class ShoppingIndex(TemplateView):
	template_name = 'info/shopping.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['farmers_market_list'] = FarmersMarket.objects.order_by('name')
		context['vegan_com_list'] = VeganCompany.objects.order_by('name')
		return context
