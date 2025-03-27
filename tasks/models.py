from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    title = models.CharField(max_length=255)  # عنوان المهمة
    description = models.TextField(blank=True, null=True)  # وصف المهمة
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')  # أولوية المهمة
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')  # حالة المهمة
    created_at = models.DateTimeField(auto_now_add=True)  # تاريخ الإضافة
    updated_at = models.DateTimeField(auto_now=True)  # تاريخ آخر تعديل
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # الشخص المسؤول عن المهمة

    def __str__(self):
        return self.title
