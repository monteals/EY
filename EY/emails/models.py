"""Emails models"""

# Django
from django.db import models

# Models
from django.contrib.auth.models import User

class Emails(models.Model):
    """Emails model"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    email = models.EmailField(unique=True)
    priority = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return email and username"""
        return '{} by @{}'.format(self.email, self.user.username)

