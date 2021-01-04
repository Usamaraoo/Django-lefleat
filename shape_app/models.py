from django.contrib.gis.db import models


# Create your models here.

class Pointing(models.Model):
    point = models.PointField(srid=4326)


class Pakistan(models.Model):
    name = models.CharField(max_length=75, null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326, null=True, blank=True)
    tag = models.CharField(max_length=40, null=True, blank=True)
    selected_color = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name


class Areas(models.Model):
    tag = models.CharField(max_length=40, null=True, blank=True)
    area = models.ManyToManyField(Pakistan,null=True,blank=True)

    def __str__(self):
        return str(self.tag)
