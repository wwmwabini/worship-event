from django.db import models
from django.utils import timezone

class Registration(models.Model):

    WORSHIP_TYPE = {
        "Solo": "Solo",
        "Choir": "Choir"
    }
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    worship_type = models.TextField(choices=WORSHIP_TYPE, default="Solo")
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.first_name + ' ' + self.last_name
