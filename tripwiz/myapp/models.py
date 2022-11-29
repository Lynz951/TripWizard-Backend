from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    # username = models.CharField(max_length=25)
    # last_login = models.DateField()
    # first_name = models.CharField(max_length=25)
    # last_name = models.CharField(max_length=40)
    # email = models.EmailField()
    # home_city = models.CharField(max_length=100)
    birthday = models.DateField(null=True)
    # country_code = models.IntegerField()
    # is_superuser = models.BooleanField()
    # is_staff = models.BooleanField()
    # is_active = models.BooleanField()
    # can_edit = models.BooleanField()
    # date_joined = models.DateField()

    def __str__(self):
        return self.username

class Trip(models.Model):
    name = models.CharField(max_length=200)
    # poi id
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name + ": " + "Dates: " + self.start_date.strftime("%m/%d/%Y") + " - " + self.end_date.strftime("%m/%d/%Y") + " Description: " + self.description