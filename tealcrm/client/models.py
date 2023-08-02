from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Client(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    description=models.TextField(blank=True, null=True)
    create_by=models.ForeignKey(User, related_name='clients', on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name