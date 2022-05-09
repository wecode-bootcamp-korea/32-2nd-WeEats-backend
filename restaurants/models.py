from django.db   import models
from core.models import TimeStampedModel

class Restaurant(models.Model):
    name            = models.CharField(max_length=500)
    category        = models.ForeignKey('Category', on_delete=models.CASCADE)
    address         = models.CharField(max_length=500, blank=True)
    latitude        = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    longitude       = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    open_time       = models.TimeField()
    close_time      = models.TimeField()
    detail_image    = models.CharField(max_length=500)
    thumbnail_image = models.OneToOneField('Restaurant_Image', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'restaurants'

class Restaurant_Image(models.Model):
    thumbnail_image = models.CharField(max_length=500)

    class Meta:
        db_table = 'restaurant_images'


class Category(models.Model):
    name = models.CharField(max_length=500)

    class Meta:
        db_table = 'categories'