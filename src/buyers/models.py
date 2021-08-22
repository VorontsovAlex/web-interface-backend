from django.db import models

from users.models import User


class Buyer(models.Model):
    """Users registered as buyers"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name