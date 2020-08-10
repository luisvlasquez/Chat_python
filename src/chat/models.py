from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


""" Models messages"""
class Message(models.Model):
    author = models.ForeignKey(User,related_name='author_message', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    #function for reload chat after 20 messages
    def last_20_messages(self):
        return Message.objects.order_by('-timestamp').all()[:20]
