from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Bleet(models.Model):
    """
    Represents a bleet.
    """

    content = models.TextField(
        "Bleet", help_text="The content of your bleet. Use Markdown."
    )
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    @property
    def number_of_comments(self):
        return Comment.objects.filter(bleet_connected=self).count()


class Comment(models.Model):
    """
    Represents a comment on a bleet.
    """

    content = models.TextField("Comment", help_text="Use Markdown.", max_length=150)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    bleet_connected = models.ForeignKey(Bleet, on_delete=models.CASCADE)
