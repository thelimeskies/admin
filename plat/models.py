from django.db import models


# Create your models here.
class PlatformUser(models.Model):
    card_id = models.CharField(unique=True, max_length=11)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=32)

    def __str__(self):
        return self.id
