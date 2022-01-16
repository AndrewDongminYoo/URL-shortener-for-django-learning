from django.db import models
from django.contrib.auth.models import User as U
from django.contrib.auth.models import AbstractUser

from shortener.urls.utils import rand_letter, rand_string


class TimeStampedModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class PayPlan(TimeStampedModel):
    name = models.CharField(max_length=20)
    price = models.IntegerField()


class Organization(TimeStampedModel):
    class Industries(models.TextChoices):
        PERSONAL = "personal"
        RETAIL = "retail"
        MANUFACTURING = "manufacturing"
        IT = "it"
        OTHERS = "others"
    name = models.CharField(max_length=50)
    industry = models.CharField(max_length=15, choices=Industries.choices, default=Industries.OTHERS)
    pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING, null=True)


class Users(AbstractUser):
    full_name = models.CharField(max_length=100, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING, null=True)
    url_count = models.IntegerField(default=0)


class EmailVerification(TimeStampedModel):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    key = models.CharField(max_length=100, null=True)
    verified = models.BooleanField(default=False)


class Categories(TimeStampedModel):
    name = models.CharField(max_length=100)
    organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING, null=True)
    creator = models.ForeignKey(Users, on_delete=models.CASCADE)


class ShortenedUrls(TimeStampedModel):
    class UrlCreatedVia(models.TextChoices):
        WEBSITE = "web"
        TELEGRAM = "telegram"
    nick_name = models.CharField(max_length=100)
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING, null=True)
    prefix = models.CharField(max_length=50, default=rand_letter)
    creator = models.ForeignKey(Users, on_delete=models.CASCADE)
    target_url = models.CharField(max_length=2000)
    shortened_url = models.CharField(max_length=6, default=rand_string)
    created_via = models.CharField(max_length=8, choices=UrlCreatedVia.choices, default=UrlCreatedVia.WEBSITE)
    expired_at = models.DateTimeField(null=True)

    class Meta:
        indexes = [
            models.Index(fields=["prefix", "shortened_url"])
        ]
