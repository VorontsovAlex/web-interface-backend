from django.db import models

from users.models import User


class Seller(models.Model):
    """Users registered as sellers"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    logo = models.CharField(max_length=255, null=True, blank=True, verbose_name='Company logo if applicable')
    website = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='Company or personal website if applicable'
    )

    def __str__(self):
        return self.user.name