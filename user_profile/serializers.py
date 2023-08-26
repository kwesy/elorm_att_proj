from rest_framework import serializers
from .models import Profile, User


class ProfileSerializer(serializers.ModelSerializer):
     class Meta:
          model = Profile
          fields = "__all__"
          read_only_fields = ['user']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    
    class Meta:
            model = User
            fields = ['id','username','email','password','first_name','last_name', 'profile']
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

        Profile.objects.create(user=user, **validated_data.pop('profile'))
        return user

    def update(self, instance:User, validated_data:dict):
        user_extra_data:dict = validated_data.pop('profile')
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.first_name = validated_data.get('first_name',instance.last_name)
        instance.save()
        # user_extra = UserExtra.objects.get(user=instance)
        # if user_extra:
        #     user_extra.profile_picture = user_extra_data.get('profile', user_extra.profile_picture)
        #     user_extra.modified_on = datetime.datetime.now()
        #     user_extra.save()

        return instance