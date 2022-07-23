from django.db import models
from users.models import User
import uuid


class Tag(models.Model):
    
    class Meta:
        db_table = 'tags'
        
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=False, max_length=255)
    
class Group(models.Model):
    
    class Meta:
        db_table = 'groups'
    
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=False, max_length=255)


class Todo(models.Model):
    
    class Meta:
        db_table = 'todos'


    class Status(models.TextChoices):
        NOT_STARTED = 'not started'
        NEXT_UP = 'next up'
        IN_PROGRESS = 'in progress'
        TO_BE_CONFIRMED = 'to be confirmed'
        COMPLETED = 'completed'        


    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(blank=False, max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, blank=True, related_name='updated_by', on_delete=models.SET_NULL, null=True)
    due_datetime = models.DateTimeField(blank=True)
    status = models.IntegerField(choices=Status.choices)
    group = models.ForeignKey(Group, blank=True, on_delete=models.SET_NULL, null=True)
    is_deleted = models.BinaryField(default=False, blank=False)
    
    
    def __str__(self):
        return self.title