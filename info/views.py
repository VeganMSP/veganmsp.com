from dal.autocomplete import Select2QuerySetView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView

from .forms import RestaurantModelForm

from blog.models import Post

from .models import (
    City,
    FarmersMarket,
    Link,
    Restaurant,
    VeganCompany,
)


class IndexView(TemplateView):
    template_name = 'info/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_posts_list'] = Post.objects.order_by(
            '-date_created'
        )[:5]
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
    template_name = 'info/restaurant_list.html'

    def get_queryset(self):
        return Restaurant.objects.order_by('location', 'name')


class AllVeganRestaurants(ListView):
    template_name = 'info/restaurant_list.html'

    def get_queryset(self):
        return Restaurant.objects.filter(
            all_vegan=True).order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'All Vegan Restaurants'
        return context


class ShoppingIndex(TemplateView):
    template_name = 'info/shopping.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['farmers_market_list'] = FarmersMarket.objects.order_by('name')
        context['vegan_com_list'] = VeganCompany.objects.order_by('name')
        return context


@login_required
def restaurant_create(request):
    if request.method == 'POST':
        form = RestaurantModelForm(request.POST)
        if form.is_valid():
            restaurant = form.save(commit=False)
            restaurant.save()
            return redirect('info:restaurant_list')
    form = RestaurantModelForm()
    return render(request, 'info/restaurant_form.html', {'form': form})


class CityAutocomplete(Select2QuerySetView):
    def get_queryset(self):
        # Filter out results depending on login state
        if not self.request.user.is_authenticated:
            return City.objects.none()

        qs = City.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


@login_required
def restaurant_update(request, slug):
    restaurant = get_object_or_404(Restaurant, slug=slug)
    form = RestaurantModelForm(request.POST or None, instance=restaurant)
    if form.is_valid():
        form.save()
        return redirect('info:restaurant_list')

    return render(request, 'info/restaurant_form.html', {'form': form})


@login_required
def restaurant_delete(request, slug):
    restaurant = get_object_or_404(Restaurant, slug=slug)
    if request.method == 'POST':
        restaurant.delete()
        return redirect('info:restaurant_list')
    return render(
        request, 'info/restaurant_delete.html',
        {'restaurant': restaurant}
    )
