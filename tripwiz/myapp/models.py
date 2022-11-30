from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=25, unique=True)
    last_login = models.DateField(null=True)
    first_name = models.CharField(max_length=25, null=True)
    last_name = models.CharField(max_length=40, null=True)
    email = models.EmailField(null=True)
    home_city = models.CharField(max_length=100, null=True)
    birthday = models.DateField(null=True)
    country_code = models.IntegerField(null=True)
    is_superuser = models.BooleanField(null=True)
    is_staff = models.BooleanField(null=True)
    is_active = models.BooleanField(null=True)
    can_edit = models.BooleanField(null=True)
    date_joined = models.DateField(null=True)

    extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

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