from django.contrib.auth import get_user_model
from rest_framework.decorators import APIView
from user_profile.serializers import UserSerializer, ProfileSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import permissions, generics


User = get_user_model()


class GetUserView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ProfileSerializer
    queryset = get_user_model().objects.all()



class CreateUserView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = {
            'username':request.data.get('username'),
            'password':request.data.get('password'),
            'email':request.data.get('email'),
            'first_name':request.data.get('first_name'),
            'last_name':request.data.get('last_name'),
            'profile':request.data.get('profile'),
            }
        
        serializer = UserSerializer(data = data)

        if serializer.is_valid(raise_exception=True):
            instance = serializer.save()
            return Response(serializer.validated_data.get('username'))


class UpdateUserView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request, format=None):
        data = {
            'first_name':request.data.get('first_name'),
            'last_name':request.data.get('last_name'),
            # 'profile':{
            #     'member_id':request.data.get('id')},
            }
        serializer = UserSerializer(instance=request.user, data =data, partial=True)

        if serializer.is_valid(raise_exception=True):
            instance = serializer.save()
            return Response(serializer.validated_data)