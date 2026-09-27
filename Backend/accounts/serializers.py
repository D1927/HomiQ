from rest_framework import serializers
from .models import User

# To sanitize and validate data from registering
class RegisterSerializer(serializers.ModelSerializer): # ModelSerializer maps the user model fields to JSON and validates them.
    password = serializers.CharField(write_only = True , min_length = 3) # write_only means just send it not get

    class Meta:
        model = User
        fields = ["id", "username" , "email", "password", "role"]

    # Create user
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create_user(password = password , **validated_data)
        return user