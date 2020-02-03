from django.contrib import admin
from .models import CustomUserModel,Vote

admin.site.register(CustomUserModel)
admin.site.register(Vote)
