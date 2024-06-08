from django.db import models
from datetime import date


class Dolor(models.Model):
    company = models.CharField(max_length=256, blank=False, default='')
    start_date = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.company}"

    class Meta:
        verbose_name_plural = "companies"


class Calendar(models.Model):
    start_date = models.DateField(default=date.today)
    dolor = models.ForeignKey(Dolor, on_delete=models.CASCADE, blank=False, default='')

    def __str__(self):
        return f"{self.start_date} - {self.dolor}"

