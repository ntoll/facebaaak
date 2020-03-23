from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Bleet(models.Model):
    """
    Represents a bleet.
    """

    content = models.TextField(
        "Bleet", help_text="The content of your bleet. Use Markdown.",
        max_length=2048
    )
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
