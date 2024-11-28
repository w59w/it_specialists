
from django.contrib.auth.models import AbstractUser
from django.db import models


class ITSpecialist(AbstractUser):
    QUALIFICATION_CHOICES = [
        ('Junior', 'Junior'),
        ('Middle', 'Middle'),
        ('Senior', 'Senior'),
    ]

    qualification = models.CharField(max_length=10, choices=QUALIFICATION_CHOICES, blank=False)
    salary = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.username} ({self.qualification}, ${self.salary})"

