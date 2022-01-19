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
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from ninja import NinjaAPI

from shrinker.settings import DEBUG
from shortener.views import index
from shortener.urls.views import url_redirect
from shortener.urls.urls import router as url_router
from shortener.users.apis import user as user_router

schema_view = get_schema_view(
    openapi.Info(
        title="Shrinker API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="ydm2790@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

apis = NinjaAPI(title="Shrinker API")
apis.add_router("/users/", user_router, tags=["Common"])

urlpatterns = [
    url(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    url(r"^swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    url(r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("", index, name="index"),
    path("admin/", admin.site.urls),
    path("users/", include("shortener.users.urls")),
    path("urls/", include("shortener.urls.urls")),
    path("api/", include(url_router.urls)),
    path("ninja-api/", apis.urls),
    path("<str:prefix>/<str:url>", url_redirect),
]

if DEBUG:
    import debug_toolbar
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),  # Django Debug Tool
    ]

