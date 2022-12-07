from django.contrib import admin
from .models import *


# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Trip)
admin.site.register(PlanType)
admin.site.register(Plan)