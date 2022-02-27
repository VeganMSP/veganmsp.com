from django.contrib import admin

from .models import (
    Address,
    City,
    FarmersMarket,
    Link,
    LinkCategory,
    Restaurant,
    VeganCompany,
)

from .forms import (
    RestaurantModelForm,
)


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_updated', 'date_created')
    search_fields = ['name', 'description']


class RestaurantAdmin(admin.ModelAdmin):
    form = RestaurantModelForm
    list_display = ('name', 'slug', 'location')
    search_fields = ['name', 'description']


admin.site.register(City, CityAdmin)
admin.site.register(Restaurant, RestaurantAdmin)


class FarmersMarketAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'hours')
    list_filter = ['address__city__name']
    search_fields = ['name']


admin.site.register(Address)
admin.site.register(FarmersMarket, FarmersMarketAdmin)
admin.site.register(VeganCompany)

admin.site.register(LinkCategory)
admin.site.register(Link)
