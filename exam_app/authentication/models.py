from django.db import models
from django.contrib.auth.models import User
from .smart_contract_integration import questionextract


class question(models.Model):
    
    title = questionextract().x
    Answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + "\n" + self.description
# Create your models here.
