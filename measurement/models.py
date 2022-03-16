from django.db import models

class Sensor(models.Model):
    name = models.TextField()
    description = models.TextField()


class Measurement(models.Model):
    temperature = models.FloatField()
    measurement_date = models.DateField(auto_now=True)
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    image = models.ImageField(blank=True)