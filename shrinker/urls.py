"""shrinker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URL conf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from shortener.urls.views import url_redirect
from shortener.views import index
from shrinker.settings import DEBUG
from shortener.urls.urls import router as url_router

urlpatterns = [
    path("", index, name="index"),
    path("admin/", admin.site.urls),
    path("users/", include("shortener.users.urls")),
    path("urls/", include("shortener.urls.urls")),
    path("api/", include(url_router.urls)),
    path("<str:prefix>/<str:url>", url_redirect),
]

if DEBUG:
    import debug_toolbar
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),  # Django Debug Tool
    ]
