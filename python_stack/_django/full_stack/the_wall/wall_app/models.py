from django.db import models
from login_app.models import User


# Create your models here.

class Message(models.Model):
    user = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(User, related_name="user_comments", on_delete=models.CASCADE)
    message = models.ForeignKey(Message, related_name="message_comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
