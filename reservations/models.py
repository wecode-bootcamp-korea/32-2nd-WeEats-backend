from django.db          import models
from core.models        import TimeStampedModel
from users.models       import User
from restaurants.models import Restaurant

class Reservation(TimeStampedModel):
    restaurant    = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user          = models.ForeignKey(User, on_delete=models.CASCADE)
    status        = models.ForeignKey('ReservationStatus', on_delete=models.CASCADE)
    date          = models.DateField()
    start_time    = models.TimeField()
    end_time      = models.TimeField()
    visitor_count = models.PositiveIntegerField()

    class Meta:
        db_table = 'reservations'

class ReservationStatus(models.Model):
    status = models.CharField(max_length=100)

    class Meta:
        db_table ='reservation_statuses'