from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import detail_route
from .models import Guide, Tour, Place, Route
from rest_framework import viewsets
from guide.serializers import GuideSerializers, TourSerializers, PlaceSerializers, RouteSerializers


# Create your views here.

class GuideViewSet(viewsets.ModelViewSet):
    queryset = Guide.objects.all().order_by('id')
    serializer_class = GuideSerializers

class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all().order_by('id')
    serializer_class = TourSerializers

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all().order_by('id')
    serializer_class = PlaceSerializers
    @detail_route(methods=['post'], url_path='create')
    def create_post(self, request, pk):
        """
            al crear un lugar para un tour debemos obtener el id del tour para enlazar.
        """
        if request.method == 'POST':
            data = JSONParser().parse(request)
            try:
                queryset = Tour.objects.get(id=data["tour_id"])
            except Tour.DoesNotExist:
                return HttpResponse("El tour no existe.",status=404)
            except:
                return HttpResponse("No veo el id tour",status=404)
            if data["tour_id"]:
                serializer = PlaceSerializers(data=data)
                if serializer.is_valid():
                    serializer.save()
                    route = Route(tour_id = data['tour_id'], place_id = serializer.data['id'])
                    route.save()
                    return JsonResponse(serializer.data, status=201)
                return JsonResponse(serializer.errors, status=400)
            return JsonResponse("No hay tour para este lugar.", status=400)

class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all().order_by('id')
    serializer_class = RouteSerializers
