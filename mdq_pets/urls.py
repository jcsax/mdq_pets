"""MDQ_Pets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from mdq_pets.views import index, Mostrar_Locales
from accounts.views import Ver_Local

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('index/', index, name = 'index'),
    path('cuenta/', include('accounts.urls')),
    path('negocios/', Mostrar_Locales.as_view(), name = 'all'),
    path('negocios/<int:pk>/', Ver_Local.as_view(), name = 'detail_local')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
