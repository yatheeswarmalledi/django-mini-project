from django.db import models

# Create your models here.
class MyUser(models.Model):
    user_id = models.CharField(primary_key=True, max_length=60)
    real_name = models.CharField(max_length=120)
    tz = models.CharField(max_length=60)

    def __str__(self):
        return self.real_name

class ActivityPeriod(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user_id = models.ForeignKey(MyUser,
                                related_name='activity',
                                on_delete=models.CASCADE)
