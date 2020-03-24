from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Represents a user's profile. Currently this only includes their bio. This
    class also makes it easy to get the followers and user following for a
    particular user.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=256)

    def __str__(self):
        return f"{self.user.username} Profile"

    @property
    def followers(self):
        return Follow.objects.filter(follow_user=self.user).count()

    @property
    def following(self):
        return Follow.objects.filter(user=self.user).count()


class Follow(models.Model):
    """
    Represents a follow relationship between two users: a target user and a
    following user.
    """
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    follow_user = models.ForeignKey(
        User, related_name="follow_user", on_delete=models.CASCADE
    )
    date = models.DateTimeField(auto_now_add=True)
