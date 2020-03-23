from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Bleet 


class BleetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bleet
        fields = ["id", "content", "date_posted" ]
