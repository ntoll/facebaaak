from django.test import TestCase
from django.contrib.auth.models import User
from .models import Bleet


class BleetModelTests(TestCase):

    def test_create_bleet(self):
        user = User.objects.create_user(username="test_user", password="12345")
        b = Bleet()
        b.content = "Hello, world!"
        b.user = user
        b.save()
        result = Bleet.objects.get(user=user)
        assert result.content == "Hello, world!"
