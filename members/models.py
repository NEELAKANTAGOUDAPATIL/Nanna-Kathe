from django.conf import settings
from django.urls import reverse
from django.db import models
from django.utils import timezone

import misaka

from django.contrib.auth import get_user_model
User = get_user_model()


class Member(models.Model):
    user = models.ForeignKey(User, related_name="members", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone = models.IntegerField(max_length=10)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=255)
    principal_amt = models.IntegerField(max_length=10)
    start_date = models.DateField(default=timezone.now().date())
    interest = models.FloatField(max_length=3)
    interest_amt = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    total_amt = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    end_date = models.DateField(null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "member_detail",
            kwargs={
                "username": self.user.username,
                "pk": self.pk
            }
        )

    class Meta:
        ordering = ["name"]
