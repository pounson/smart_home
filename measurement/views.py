from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer


class SensorListCreate(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def list(self, request):
        sensor_list = SensorSerializer(self.queryset.all(), many=True)
        return Response(sensor_list.data)

    def create(self, request):
        sensor_new = SensorSerializer(data=request.data)
        if sensor_new.is_valid():
            sensor_new.save()
            return Response('Ок')


class SensorRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def update(self, request, pk=None):
        sensor_pk = SensorDetailSerializer(Sensor.objects.get(pk=pk), data=request.data)
        if sensor_pk.is_valid():
            sensor_pk.save()
            return Response('Ок')

    def retrieve(self, request, pk=None):
        sensor_pk = SensorDetailSerializer(Sensor.objects.get(pk=pk))
        return Response(sensor_pk.data)


class MeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def create(self, request):
        measurement_new = MeasurementSerializer(data=request.data)
        if measurement_new.is_valid():
            measurement_new.save()
            return Response('Ок')