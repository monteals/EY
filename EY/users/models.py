"""Users models"""

"""Django"""
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile (models.Model):
    """Modelo de perfil
    Modelo que se extiende de la base de Django con otra informacion    
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=20)
    first_last_name = models.CharField(max_length=20)
    second_last_name = models.CharField(max_length=20, blank=True)

    identification = models.CharField(max_length=10)
    age = models.CharField(max_length=3)

    gender_choices = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('Ot', 'Other'),
        ('NA', 'N/A'),
    )
    gender = models.CharField(max_length=2, choices=gender_choices)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username"""
        return self.user.username

