from django.db   import models
from core.models import TimeStampedModel

class User(TimeStampedModel):
    kakao_id      = models.BigIntegerField()
    name          = models.CharField(max_length=100)
    profile_image = models.CharField(max_length=1000)
    email         = models.CharField(max_length=1000)

    class Meta :
        db_table = 'users'
