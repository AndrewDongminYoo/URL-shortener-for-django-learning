from django.db import models
from django.contrib.auth.models import User as U
from django.contrib.auth.models import AbstractUser
import string
import random

# Create your models here.


class TimeStampedModels(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)


class PayPlan(TimeStampedModels):
    name = models.CharField(max_length=20)
    price = models.IntegerField()


class Users(AbstractUser):
    full_name = models.CharField(max_length=100, null=True)
    pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING, null=True)


def rand_string():
    str_pool = string.digits + string.ascii_letters
    return "".join([random.choice(str_pool) for _ in range(6)])


class ShortenedUrls(TimeStampedModels):
    class UrlCreatedVia(models.TextChoices):
        WEBSITE = "web"
        TELEGRAM = "telegram"
    nick_name = models.CharField(max_length=100)
    created_by = models.ForeignKey(Users, on_delete=models.CASCADE)
    target_url = models.CharField(max_length=2000)
    shortened_url = models.CharField(max_length=6, default=rand_string)
    created_via = models.CharField(max_length=8, choices=UrlCreatedVia.choices, default=UrlCreatedVia.WEBSITE)
