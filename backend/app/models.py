from django.db import models

# Create your models here.




class Todo(models.Model):
    title = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title
        
