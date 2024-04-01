from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    additional_info = models.TextField(blank=True)

class UserQuery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='queries')
    query_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
class ChatResponse(models.Model):
    query = models.ForeignKey(UserQuery, on_delete=models.CASCADE, related_name='responses')
    response_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)