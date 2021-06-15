from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def points_recieved(self, user):
        # THis needs to be updated with the actual points
        return 2


class Criteria(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    max_points = models.IntegerField(null=True, blank=True)
    short_description = models.TextField(null=True, blank=True)
    long_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Criteria'

    def points_recieved(self, user):
        # THis needs to be updated with the actual points
        return 2


class Subcriteria(models.Model):
    criteria = models.ForeignKey(Criteria, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    max_points = models.IntegerField(default=1)
    short_description = models.TextField(null=True, blank=True)
    long_description = models.TextField(null=True, blank=True)
    subsume = models.ForeignKey(
        'Subcriteria', related_name='subsumed_by', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Subcriteria'

    def points_recieved(self, user):
        house, created = House.objects.get_or_create(user=user)
        points, created = HousePoints.objects.get_or_create(
            house=house, subcriteria=self)
        return points.points


class House(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(House, self).save(*args, **kwargs)

    def total_points(self):
        ''' Calculates the total points for the house. '''
        points = HousePoints.objects.filter(house=self)
        # Todo: make the calculation consider max points
        return sum([p.points for p in points])


class HousePoints(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    subcriteria = models.ForeignKey(Subcriteria, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return ""

    class Meta:
        ordering = []
        verbose_name = "User Points"
        verbose_name_plural = "User Points"
