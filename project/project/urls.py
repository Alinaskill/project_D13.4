from django.contrib import admin
from django.urls import path, include
from simpleapp.views import add_subscribe, delete_subscribe
from django.views.decorators.cache import cache_page


urlpatterns = [
   path('admin/', admin.site.urls),
   path('pages/', include('django.contrib.flatpages.urls')),
   # Делаем так, чтобы все адреса из нашего приложения (simpleapp/urls.py)
   # подключались к главному приложению с префиксом news/.
   path('news/', include('simpleapp.urls')),
   path('', include('protect.urls')),
   path('sign/', include('sign.urls')),
   path('accounts/', include('allauth.urls')),
]

#<int:pk>