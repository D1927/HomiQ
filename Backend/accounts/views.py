from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

# The api endpoint to register user
class RegisterView(APIView):
    def post(self, request): # Here we are also mentioning the method we want --- for ex post
        serializer = RegisterSerializer(data = request.data) # Validate it 

        if serializer.is_valid():
            user = serializer.save()
            return Response({
                    "message": "User registered successfully",
                    "user": {
                        "id": user.id,
                        "username": user.username,
                        "email": user.email,
                        "role": user.role
                    }
                },
                status = status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
        )

# To authenticate user using JWT
class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(request , username=username , password=password) # check them

        if user is None:
            return Response(
                {"error": "Invalid username or password"},
                status = status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user) # Creates new JWT

        return Response({
                "message": "Login successful",
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "role": user.role
                },
                "tokens": {
                    "refresh": str(refresh), # Access token - short lived
                    "access": str(refresh.access_token) # It is refreshed after above is expired -- it often long for a day 
                }
            },
            status = status.HTTP_200_OK
        )