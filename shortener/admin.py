from django.contrib import admin
from shortener.models import Statistic
from shortener.models import PayPlan
from shortener.models import Users

# Register your models here.

admin.site.register(PayPlan)
admin.site.register(Users)
admin.site.register(Statistic)
