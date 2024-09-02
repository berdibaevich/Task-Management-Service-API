from rest_framework import serializers

from .models import Account


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    password2 = serializers.CharField()

    class Meta:
        model = Account
        fields = ("username", "password", "password2")

    def validate(self, attrs):
        data = super().validate(attrs)
        if data.get("password") != data.get("password2"):
            raise serializers.ValidationError("Passwords do not match")
        return data
    
    def create(self, validated_data):
        username = validated_data.get("username")
        user = Account.objects.create(username = username)
        user.set_password(validated_data.get("password"))
        user.save()
        return user
    

