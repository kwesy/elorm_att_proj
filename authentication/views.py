from django.contrib.auth import login, logout
from rest_framework import permissions
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serializer import LoginSerializer


# Create your views here.

class LoginView(APIView):

        permission_classes = (permissions.AllowAny,)

        def post(self, request, format=None):
            serializer = LoginSerializer(data=self.request.data,
                context={ 'request': self.request })
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            login(request, user)
            return Response(serializer.validated_data.get('username'), status=200)


class LogoutView(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
            logout(request)
            return Response('logout successfull')
