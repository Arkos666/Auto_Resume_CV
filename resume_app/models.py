# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import date


class Company(models.Model):
    company = models.CharField(max_length=256, blank=False, default='')

    def __str__(self):
        return f"{self.company}"

    class Meta:
        verbose_name_plural = "companies"


class Position(models.Model):
    position = models.CharField(max_length=64, blank=False)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=False, default='')

    def __str__(self):
        return f"{self.company} - {self.position}"


class TagJob(models.Model):
    tag = models.CharField(max_length=24, blank=False)

    def __str__(self):
        return f"{self.tag}"


class Action(models.Model):
    action = models.TextField(blank=False)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, blank=False, default='')
    tag_job = models.ManyToManyField(TagJob)

    def __str__(self):
        return f"{self.action}"


class Skill(models.Model):
    skill = models.CharField(max_length=30)
    tag_job = models.ManyToManyField(TagJob)

    def __str__(self):
        return f"{self.skill}"


class Education(models.Model):
    education = models.CharField(max_length=30)
    end_date = models.DateField(default=date.today)
    tag_job = models.ManyToManyField(TagJob)

    def __str__(self):
        return f"{self.education}"

    class Meta:
        verbose_name_plural = "education"


class CvTemplate(models.Model):
    title = models.CharField(max_length=30)

