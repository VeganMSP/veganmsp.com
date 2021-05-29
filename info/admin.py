from django.contrib import admin

from .models import City, Neighborhood, Restaurant, Address, FarmersMarket, RestaurantLocation


class CityAdmin(admin.ModelAdmin):
	list_display = ('name', 'date_updated', 'date_created')
	search_fields = ['name', 'description']


class NeighborhoodAdmin(admin.ModelAdmin):
	list_display = ('name', 'city', 'date_updated', 'date_created')
	list_filter = ['city']
	search_fields = ['name', 'city__name']


class RestaurantAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug', 'location')
	search_fields = ['name', 'description']


admin.site.register(RestaurantLocation)
admin.site.register(City, CityAdmin)
admin.site.register(Neighborhood, NeighborhoodAdmin)
admin.site.register(Restaurant, RestaurantAdmin)


class FarmersMarketAdmin(admin.ModelAdmin):
	list_display = ('name', 'address', 'hours')
	list_filter = ['address__city__name']
	search_fields = ['name']


admin.site.register(Address)
admin.site.register(FarmersMarket, FarmersMarketAdmin)
