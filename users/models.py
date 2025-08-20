from django.contrib.auth.models import AbstractUser, Group
from django.db import models

class CustomUser(AbstractUser):
    is_creator = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.is_creator:
            creator_group, _ = Group.objects.get_or_create(name='Creator')
            self.groups.add(creator_group)
        else:
            consumer_group, _ = Group.objects.get_or_create(name='Consumer')
            self.groups.add(consumer_group)