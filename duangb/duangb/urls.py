"""
URL configuration for duangb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, re_path, include
# loi :(
from ungdunggb.admin import admin_site
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Ecommerce API",
        default_version='v1',
        description="APIs for EcommerceApp",
        contact=openapi.Contact(email="chanhkhoi2003@gmail.com"),
        license=openapi.License(name="Nguyễn Chánh Khôi@2024"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('ungdunggb.urls')),

    path('admin/', admin_site.urls),

    path('o/', include('oauth2_provider.urls',namespace='oauth2_provider')),

    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),

    path("__debug__/", include("debug_toolbar.urls")),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
            name='schema-json'),

    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'),

    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc')
]
