from django.db import models


class CityWeather(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Город")
    latitude = models.DecimalField(decimal_places=4, verbose_name="Широта")
    longitude = models.DecimalField(decimal_places=4, verbose_name="Долгота")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    weather_condition = models.JSONField(null=True, verbose_name="Погода (JSON)")

    def __str__(self) -> str:
        return self.name
