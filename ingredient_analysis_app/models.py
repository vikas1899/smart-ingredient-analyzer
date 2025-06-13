# ingredient_analysis_app/models.py

from django.db import models
from django.contrib.auth.models import User


class IngredientAnalysis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    result = models.TextField()
    # Automatically adds the current timestamp
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']  # descending order

    def __str__(self):
        return f"{self.user.username} - {self.category} - {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
