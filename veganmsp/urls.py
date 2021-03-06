"""veganmsp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path

from pages.views import PageView

urlpatterns = [
    path('', include('info.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    re_path(
        r'^invitations/',
        include('invitations.urls', namespace='invitations'),
    ),
    re_path(
        r'^.*|<page:page>/',
        PageView.as_view(),
        name='page_view',
    ),
]
