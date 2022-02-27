from dal.autocomplete import Select2QuerySetView
from django.views.generic import TemplateView, ListView

from generic.views import (
    BaseAddView,
    BaseAddViewWithAddressForm,
    BaseAddViewWithLinkCategoryForm,
    SlugEditView,
    SlugEditViewWithAddressForm,
    SlugDeleteView,
    SlugEditViewWithLinkCategoryForm,
)

from .forms import (
    BaseFarmersMarketForm,
    BaseLinkForm,
    BaseRestaurantForm,
    BaseVeganCompanyForm,
    FarmersMarketAddForm,
    LinkAddForm,
    RestaurantAddForm,
    VeganCompanyAddForm
)

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


class RestaurantCreate(BaseAddView):
    form_class = RestaurantAddForm
    template_name = 'info/restaurant_form.html'
    redirect_target = 'info:restaurant_list'


class CityAutocomplete(Select2QuerySetView):
    def get_queryset(self):
        # Filter out results depending on login state
        if not self.request.user.is_authenticated:
            return City.objects.none()

        qs = City.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


class RestaurantUpdate(SlugEditView):
    model_class = Restaurant
    form_class = BaseRestaurantForm
    template_name = 'info/restaurant_form.html'
    redirect_target = 'info:restaurant_list'


class RestaurantDelete(SlugDeleteView):
    model_class = Restaurant
    template_name = 'info/restaurant_delete.html'
    redirect_target = 'info:restaurant_list'


class ShoppingIndex(TemplateView):
    template_name = 'info/shopping_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['farmers_market_list'] = FarmersMarket.objects.order_by('name')
        context['vegan_com_list'] = VeganCompany.objects.order_by('name')
        return context


class VeganCompanyCreate(BaseAddView):
    form_class = VeganCompanyAddForm
    template_name = 'info/vegan_company_form.html'
    redirect_target = 'info:shopping_index'


class VeganCompanyUpdate(SlugEditView):
    model_class = VeganCompany
    form_class = BaseVeganCompanyForm
    template_name = 'info/vegan_company_form.html'
    redirect_target = 'info:shopping_index'


class VeganCompanyDelete(SlugDeleteView):
    model_class = VeganCompany
    template_name = 'info/generic_delete.html'
    redirect_target = 'info:shopping_index'


class FarmersMarketCreate(BaseAddViewWithAddressForm):
    form_class = FarmersMarketAddForm
    template_name = 'info/farmers_market_form.html'
    redirect_target = 'info:shopping_index'


class FarmersMarketUpdate(SlugEditViewWithAddressForm):
    model_class = FarmersMarket
    form_class = BaseFarmersMarketForm
    template_name = 'info/farmers_market_form.html'
    redirect_target = 'info:shopping_index'


class FarmersMarketDelete(SlugDeleteView):
    model_class = FarmersMarket
    template_name = 'info/generic_delete.html'
    redirect_target = 'info:shopping_index'


class LinkCreate(BaseAddViewWithLinkCategoryForm):
    form_class = LinkAddForm
    template_name = 'info/link_form.html'
    redirect_target = 'info:links_index'


class LinkUpdate(SlugEditViewWithLinkCategoryForm):
    model_class = Link
    form_class = BaseLinkForm
    template_name = 'info/link_form.html'
    redirect_target = 'info:links_index'


class LinkDelete(SlugDeleteView):
    model_class = Link
    template_name = 'info/generic_delete.html'
    redirect_target = 'info:links_index'
