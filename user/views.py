from django.contrib.auth import login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .serializers import *
from .validations import *


class UserRegister(APIView):
	permission_classes = (permissions.AllowAny,)
	def post(self, request):
		data = custom_validation(request.data)
		serializer = UserRegisterSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			user = serializer.create(data)
			token = Token.objects.create(user=user)
			if user:
				return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
	permission_classes = (permissions.AllowAny,)
	def post(self, request):
		data = request.data
		assert validate_email(data)
		assert validate_password(data)
		serializer = UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			user = serializer.check_user(data)
			login(request, user)
			token, created = Token.objects.get_or_create(user=user)
			send = {"email": user.email, "username": user.username, "password": serializer.data["password"]}
			# return Response(serializer.data, status=status.HTTP_200_OK)
			return Response({"token": token.key, "user": send}, status=status.HTTP_200_OK)
		
class UserLogout(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	def post(self, request):
		logout(request)
		return Response(status=status.HTTP_200_OK)


class UserView(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	##
	def get(self, request):
		serializer = UserSerializer(request.user)
		return Response({'user': serializer.data}, status=status.HTTP_200_OK)