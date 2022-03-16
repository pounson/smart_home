from django.urls import path
from .views import SensorListCreate, SensorRetrieveUpdate, MeasurementView
urlpatterns = [
    path('sensors/', SensorListCreate.as_view()),
    path('sensors/<pk>/', SensorRetrieveUpdate.as_view()),
    path('measurements/', MeasurementView.as_view()),

]
