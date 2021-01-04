"""gic URL Configuration

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
from django.urls import path,include
from .views import home

from bd.views import login_view, register_view, logout_view, sodesh,homeso,more_information

from django.conf.urls import url, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', include('bd.urls')),
    path('home/',home),
    path('accounts/login/', login_view),
    path('accounts/register/', register_view),
    path('accounts/logout/', logout_view),
    path('sodeshDat/',homeso),
    path('more_infortion/',more_information),
# adminlte part
    url(r'^$', TemplateView.as_view(template_name='adminlte/index.html')),
    url(r'^login/$', TemplateView.as_view(template_name='adminlte/login.html')),
    path('admin/', admin.site.urls),

]
