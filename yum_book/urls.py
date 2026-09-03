"""
URL configuration for yum_book project.

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
from django.shortcuts import render
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from recipes.views import admin_actions_log

urlpatterns = [
    path('admin/logs/', admin.site.admin_view(admin_actions_log),
         name='admin-actions-log'),
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


def custom_404(request, exception):
    return render(request, 'recipes/404.html', status=404)


handler404 = 'yum_book.urls.custom_404'
