from django.db import models

class Review(models.Model):
    full_name = models.CharField(max_length=60, blank=False)
    email = models.EmailField (blank=False)
    text = models.TextField (blank=False)
    verification = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.full_name} - {self.email}'