
from rest_framework import serializers
from .models import *
from pprint import pprint as p

# class CustomUserSerializer(AbstractUser):
    # some_relationship_fk = SomeRelationshipSerializer(required=False)   
    # class Meta:
    #     model = CustomUser
    #     fields = (
    #         'username',
    #         'last_login'
    #         'email',
    #         'username',
    #         'first_name',
    #         'last_name',
    #         'home_city',
    #         'birthday',
    #         'country_code',
    #         'is_superuser',
    #         'is_staff',
    #         'is_active',
    #         'can_edit',
    #         'date_joined',
    #     )
    # extra_kwargs = {'password': {'write_only': True}}

    # def create(self, validated_data):
    #     password = validated_data.pop('password', None)
    #     instance = self.Meta.model(**validated_data) 
    #     if password is not None:
    #         instance.set_password(password)
    #     instance.save()
    #     return instance


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'