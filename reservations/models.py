from django.db          import models
from core.models        import TimeStampedModel
from users.models       import User
from restaurants.models import Restaurant

class Reservation(TimeStampedModel):
    restaurant    = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user          = models.ForeignKey(User, on_delete=models.CASCADE)
    status        = models.ForeignKey('ReservationStatus', on_delete=models.CASCADE)
    date          = models.DateField()
    
    TIMESLOT_LIST = (
        (1, "17:00 - 19:00"),
        (2, "19:00 - 21:00"),
        (3, "21:00 - 23:00"),
    )

    timeslot = models.IntegerField(choices=TIMESLOT_LIST)

{
    1 : "12:00",
    2 : "12:30",
    3 : "13:00"
}

    visitor_count = models.PositiveIntegerField()

    class Meta:
        db_table = 'reservations'

class ReservationStatus(models.Model):
    status = models.CharField(max_length=100)

    class Meta:
        db_table ='reservation_statuses'