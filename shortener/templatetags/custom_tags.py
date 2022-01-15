from django import template
from django.utils.html import mark_safe
from datetime import time, datetime, date, timedelta
import re

register = template.library.Library()


@register.filter(name="email_masker")
def email_masker(value):
    email_split = value.split("@")
    username = email_split[0]
    covered = re.sub(r"\w", "*", email_split[1])
    return username + "@" + covered
