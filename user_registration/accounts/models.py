from django.db import models

class DynamicRow(models.Model):
    data = models.JSONField(default=dict)  # Works with MySQL 5.7+ and Django 3.1+
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Row {self.id}"
