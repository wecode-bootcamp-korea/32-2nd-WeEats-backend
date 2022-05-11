from django.db          import models
from core.models        import TimeStampedModel
from users.models       import User
from restaurants.models import Restaurant

class Review(TimeStampedModel):
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    content    = models.TextField(blank=True)

    class Meta:
        db_table = 'reviews'

class Review_Image(TimeStampedModel):
    url    = models.CharField(max_length=1000)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)

    class Meta:
        db_table = 'review_images'