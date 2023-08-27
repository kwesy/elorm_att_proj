from rest_framework import serializers
from .models import Profile, User


class ProfileSerializer(serializers.ModelSerializer):
     class Meta:
          model = Profile
          fields = "__all__"


class UserSerializer(serializers.ModelSerializer):    
    class Meta:
            model = User
            fields = ['id','username','email','password','first_name','last_name']
            extra_kwargs = {'password': {'write_only':True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    def update(self, instance:User, validated_data:dict):
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.first_name = validated_data.get('first_name',instance.last_name)
        instance.save()
        return instance