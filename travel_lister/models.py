from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.TextField(max_length=500)
    uid = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name