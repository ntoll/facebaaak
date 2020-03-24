from django.contrib import admin
from .models import Profile, Follow

# Register the models for use in the admin site.
admin.site.register(Profile)
admin.site.register(Follow)
