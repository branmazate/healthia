import openai
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class DetectedSymptom(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='detected_symptoms')
    symptom_text = models.CharField(max_length=250)
    standardized_symptom = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.symptom_text
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