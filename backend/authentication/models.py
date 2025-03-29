from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'admin'
        RECRUITER = 'recruiter'
        CANDIDATE = 'candidate'

    base_role = Role.ADMIN
    role = models.CharField(max_length=20, default=base_role, choices=Role.choices)
    def __str__(self):
        return f"{self.username} ({self.role})"
    

# START OF RECRUITER
class RecruiterManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.RECRUITER)

class Recruiter(User):
    base_role = User.Role.RECRUITER
    recruiter = RecruiterManager()
    class Meta:
        proxy = True

@receiver(post_save, sender=Recruiter)
def create_recruiter_profile(sender, instance, created, **kwargs):
    user = instance
    if created and instance.role == User.Role.RECRUITER:
        print("Recruiter Profile created successfully:")
        # Add any additional logic for creating a recruiter profile here

# END OF RECRUITER