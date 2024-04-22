from django.db import models

import tasks.models


class BugReport(models.Model):
    STATUS_CHOICES = [
        ('New', 'Новая'),
        ('In_progress', 'В работе'),
        ('Completed', 'Завершена'),
    ]
    PRIORITY_STATUS = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    title = models.CharField(max_length = 50)
    description = models.TextField()
    project = models.ForeignKey(
        tasks.models.Project,
        on_delete=models.CASCADE,
    )
    task = models.ForeignKey(
        tasks.models.Task,
        on_delete=models.SET_NULL,
        null = True,
        blank=True
    )
    status = models.CharField(
        max_length=50,
        choices = STATUS_CHOICES,
        default='New'
    )
    priority = models.CharField(
        max_length=50,
        choices=PRIORITY_STATUS,
        default='1'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class FeatureRequest(models.Model):
    STATUS_CHOICES = [
        ('Consideration', 'Рассмотрение'),
        ('Accepted', 'Принято'),
        ('Rejected', 'Отклонено'),
    ]
    PRIORITY_STATUS = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    title = models.CharField(max_length=50)
    description = models.TextField()
    project = models.ForeignKey(
        tasks.models.Project,
        on_delete=models.CASCADE,
    )
    task = models.ForeignKey(
        tasks.models.Task,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New'
    )
    priority = models.CharField(
        max_length=50,
        choices=PRIORITY_STATUS,
        default='1'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)