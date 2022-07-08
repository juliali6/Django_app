from django.contrib.auth.models import User
from django.db import models


class Friendship(models.Model):
    """Model for friendship."""

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')

    def __str__(self):
        return f'sender:{self.sender}->receiver:{self.receiver}'
