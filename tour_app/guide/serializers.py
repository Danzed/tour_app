from rest_framework import serializers
from .models import Guide, Place, Tour, Route

class GuideSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Guide
        fields = ('name', 'last_name', 'email', 'phone', 'whatsapp', 'gender','age')

class PlaceSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = ('id','name_place', 'description', 'latitude', 'longitude')

class TourSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tour
        fields = ('name_tour')

class RouteSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Route
        fields = ('tour', 'place')
