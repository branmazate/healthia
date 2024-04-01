from django.contrib import admin
from .models import UserProfile, UserQuery, ChatResponse

admin.site.register(UserProfile)
admin.site.register(UserQuery)
admin.site.register(ChatResponse)