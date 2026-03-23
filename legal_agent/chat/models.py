from django.db import models
from django.contrib.auth.models import User


# class ChatSession(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chats")
#     title = models.CharField(max_length=255, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Chat {self.id} - {self.user.username}"

class ChatSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # ✅ ADD THIS

    def __str__(self):
        return self.title or f"Chat {self.id}"


class ChatMessage(models.Model):
    chat = models.ForeignKey(
        ChatSession,
        on_delete=models.CASCADE,
        related_name="messages"
    )
    role = models.CharField(
        max_length=20,
        choices=[
            ("user", "User"),
            ("assistant", "Assistant"),
        ]
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.role} message in Chat {self.chat.id}"

