#from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    Rooms = models.IntegerField()
    Bathroom = models.IntegerField()
    Landsize = models.IntegerField()
    BuildingArea = models.IntegerField() 
    YearBuilt = models.IntegerField() 
    
    buildç_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.author
