from django.db import models
import uuid
# Tugas 4
from django.contrib.auth.models import User


class Attribute(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    # Tugas 4
    user = models.ForeignKey(User, on_delete=models.CASCADE)


# Create your models here.
