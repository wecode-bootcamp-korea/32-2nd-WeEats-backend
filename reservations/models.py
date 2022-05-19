from django.db          import models
from core.decorator     import log_in_decorator
from core.models        import TimeStampedModel
from users.models       import User
from restaurants.models import Restaurant

class Reservation(TimeStampedModel):
    TIMESLOT_LIST = (
        (1, "12:00 - 14:00"),
        (2, "14:00 - 16:00"),
        (3, "16:00 - 18:00"),
        (4, "18:00 - 20:00"),
        (5, "20:00 - 22:00"),
    )
    restaurant    = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user          = models.ForeignKey(User, on_delete=models.CASCADE)
    status        = models.ForeignKey('ReservationStatus', on_delete=models.CASCADE)
    date          = models.DateField()
    timeslot      = models.IntegerField(choices=TIMESLOT_LIST)
    visitor_count = models.PositiveIntegerField()

    class Meta:
        db_table = 'reservations'
        constraints = [models.UniqueConstraint(
            fields=['restaurant', 'date', 'timeslot'], 
            name='unique_reservation'
        )]

class ReservationStatus(models.Model):
    status = models.CharField(max_length=100)

    class Meta:
        db_table = 'reservation_statuses'