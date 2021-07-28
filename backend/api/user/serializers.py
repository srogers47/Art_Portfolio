from rest_framework import serializers
from rest_framework.decorators import authentication_classes, permission_classes
from django.contrib.auth.hashers import make_password
from .models import CustomUser

class UserSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        password = validated_data.pop('password') 
        instance = self.Meta.model(**validated_data) #instance of user
        if password is not None:
            instance.set_password(password)
            instance.save() 
            return instance

    def update(self, instance, validated_data):
       #instance.email = validated_data.email.get('email', instance.email)  ###From docs, can be improved with conditional logic control flow 
       #instance.content = validated_data.email.get('content', instance.content)
       #instance.created = validated_data.email.get('created', instance.created)
        for attr, value in validated_data.items():
            if attr == 'password': #For local dev, change in production. 
                instance.set_password(value) #NOTE: for security, only use this method, set_password for setting password. 
            else:
                setattr(instance, attr, value)
            instance.save()
            return instance

    class Meta:
        model = CustomUser
        extra_kwargs = {'password': {'write_only':True}}
        fields = (
                'name', 'email', 'password', 'phone', 'gender', 
                'is_active', 'is_staff', 'is_superuser'
                )
