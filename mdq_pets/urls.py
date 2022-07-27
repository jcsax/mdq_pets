
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from mdq_pets.views import index, Mostrar_Locales, Ver_Local

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('index/', index, name = 'index'),
    path('cuenta/', include('accounts.urls')),
    path('negocios/', Mostrar_Locales.as_view(), name = 'all'),
    path('negocios/detalle/<int:pk>/', Ver_Local.as_view(), name = 'local'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
