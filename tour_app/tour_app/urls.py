
#from django.conf.urls import url
from django.contrib import admin

from django.conf.urls import url, include
from rest_framework import routers
from guide import views

router = routers.DefaultRouter()
router.register(r'guides', views.GuideViewSet)
router.register(r'tours', views.TourViewSet)
router.register(r'places', views.PlaceViewSet)
router.register(r'routes', views.RouteViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
