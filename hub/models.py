"""
hub/models.py
"""

from django.db import models

class Resource(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    content = models.TextField()
    url = models.URLField(max_length=100)

    res_type = (
        ('education', 'Education'),
        ('job', 'Job'),
        ('technology', 'Technology'),
        ('social', 'Social'),
        ('housing', 'Housing')
    )
    res = models.CharField(max_length=15, choices=res_type, default=None)

    def __str__(self):
        return self.title