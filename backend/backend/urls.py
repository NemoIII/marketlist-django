from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from marketList import views

router = routers.DefaultRouter()
router.register(r'marketlist', views.MarketListView, 'marketlist')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
