from django.urls import path

from . import views

app_name = 'info'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('links/', views.LinkIndex.as_view(), name='links_index'),
    path(
        'restaurants/', views.RestaurantIndex.as_view(),
        name='restaurant_list'
    ),
    path(
        'restaurants/all-vegan/',
        views.AllVeganRestaurants.as_view(),
        name='all_vegan_list'
    ),
    path(
        'restaurant/add', views.RestaurantCreate.as_view(),
        name='restaurant_create'
    ),
    path(
        'restaurant/edit/<slug:slug>', views.RestaurantUpdate.as_view(),
        name='restaurant_update'
    ),
    path(
        'restaurant/delete/<slug:slug>', views.RestaurantDelete.as_view(),
        name='restaurant_delete'
    ),
    path('shopping/', views.ShoppingIndex.as_view(), name='shopping_index'),
    path(
        'vegan-company/add',
        views.VeganCompanyCreate.as_view(),
        name='vegan_com_create'
    ),
    path(
        'vegan-company/edit/<slug:slug>',
        views.VeganCompanyUpdate.as_view(),
        name='vegan_com_update'
    ),
    path(
        'vegan-company/delete/<slug:slug>',
        views.VeganCompanyDelete.as_view(),
        name='vegan_com_delete'
    ),
    path(
        'farmers-market/add',
        views.FarmersMarketCreate.as_view(),
        name='farmers_market_create'
    ),
    path(
        'farmers-market/edit/<slug:slug>',
        views.FarmersMarketUpdate.as_view(),
        name='farmers_market_update'
    ),
    path(
        'farmers-market/delete/<slug:slug>',
        views.FarmersMarketDelete.as_view(),
        name='farmers_market_delete'
    ),
    path(
        'link/add',
        views.LinkCreate.as_view(),
        name='link_create'
    ),
    path(
        'link/edit/<slug:slug>',
        views.LinkUpdate.as_view(),
        name='link_update'
    ),
    path(
        'link/delete/<slug:slug>',
        views.LinkDelete.as_view(),
        name='link_delete'
    ),
    path(
        'city-autocomplete/',
        views.CityAutocomplete.as_view(create_field='name'),
        name='city-autocomplete'
    ),
]
