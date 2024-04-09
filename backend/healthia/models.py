from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    additional_info = models.TextField(blank=True)
    
    def __str__(self):
        return self.user.username

class UserQuery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='queries')
    query_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Query by {self.user.user.username} at {self.timestamp}"
    
class ChatResponse(models.Model):
    query = models.ForeignKey(UserQuery, on_delete=models.CASCADE, related_name='responses')
    response_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Response to {self.query.user.user.username} at {self.timestamp}"