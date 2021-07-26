from django.db import models

class GroupMessage(models.Model):
    content = models.TextField()
    groupName = models.CharField(max_length=32)
    created  = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.content

    def last_messages():
        return GroupMessage.objects.all()[:20]
