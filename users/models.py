
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


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


@receiver(pre_save, sender=ITSpecialist)
def assign_salary(sender, instance, **kwargs):
    salary_mapping = {'Junior': 300, 'Middle': 1000, 'Senior': 2000}
    instance.salary = salary_mapping.get(instance.qualification, 0)
