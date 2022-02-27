from django.urls import path, re_path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path(
        'category-autocomplete/',
        views.CategoryAutocomplete.as_view(create_field='name'),
        name='category-autocomplete'
    ),
    path('_c/', views.post_create, name='post_create'),
    path('_u/<slug:slug>/', views.post_update, name='post_update'),
    path('_d/<slug:slug>/', views.post_delete, name='post_delete'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

    path(
        'category/<slug:slug>/',
        views.category_detail,
        name='category_detail',
    ),
    re_path(
        r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/(?P<slug>[\w-]+)$',  # noqa: E501
        views.PostDetailByDate.as_view(),
        name='post_detail_by_date'
    ),
]
