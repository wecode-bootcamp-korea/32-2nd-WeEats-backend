from django.db   import models
from core.models import TimeStampedModel

class User(TimeStampedModel):
    kakao_id = models.BigIntegerField()

    class Meta :
        db_table = 'users'