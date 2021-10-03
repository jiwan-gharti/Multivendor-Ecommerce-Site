"""NewAgeShopping URL Configuration

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
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('mainapp.urls')),
    path('admin/', admin.site.urls),
     path('accounts/', include('accounts.urls',namespace="accounts")),
    path('accounts/', include('allauth.urls')),
   
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('myprofile/', include('myprofile.urls', namespace="myprofile")),
    path("merchant/",include("merchant_app.urls", namespace="merchant_app")),
    path('summernote/', include('django_summernote.urls'))
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

admin.site.site_header = 'New Age Shopping'
admin.sites.AdminSite.index_title = 'New Age Shopping'
admin.site.site_title = 'Admin panel'
