from django.contrib.auth import logout
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from user.serializers import UserSerializer, UserLoginSerializer


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            return Response({'message': 'User registered successfully.', 'data': serializer.data, 'status': 200},
                            status=200)
        except Exception as e:
            return Response({'error': str(e)}, status=400)


class UserLoginView(APIView):
    def post(self, request):
        try:
            serializer = UserLoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            # Perform additional actions upon successful login if needed
            return Response({'message': 'Login successful'}, status=200)
        except Exception as e:
            return Response({'error': str(e)}, status=400)


class UserLogoutView(APIView):
    def get(self, request):
        try:
            logout(request)
            return Response({"Message": "User logout successfully"}, status=200)
        except Exception as e:
            # logging.error(e)
            return Response({"message": str(e)}, status=400)