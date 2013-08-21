from django.db import models

from model_utils.models import TimeStampedModel

class Food(TimeStampedModel):
	brand = models.CharField(max_length=100)