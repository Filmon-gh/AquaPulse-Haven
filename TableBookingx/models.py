from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

# Reservation Model
# Represents a reservation made by a user at the restaurant.
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField()  
    date = models.DateField()
    time = models.TimeField()
    party_size = models.PositiveIntegerField()
    phone = models.CharField(max_length=15, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.date} - {self.time}"

class UIElement(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = CloudinaryField('image')

    def __str__(self):
        return self.name        