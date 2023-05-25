from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from .models import Customer

User = get_user_model()


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('address', 'phone_number')


class UserSerializer(serializers.ModelSerializer):
    customer_details = CustomerSerializer(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'role', 'customer_details')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        role = validated_data.get('role')
        customer_details_data = validated_data.pop('customer_details', None)

        if role == 'admin':
            user = User.objects.create_superuser(**validated_data)
        else:
            user = User.objects.create_user(**validated_data)

        if customer_details_data:
            Customer.objects.create(user=user, **customer_details_data)

        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128, write_only=True)

    def create(self, validated_data):
        user = authenticate(username=validated_data['username'], password=validated_data['password'])
        # is_active is property
        if not user:
            raise serializers.ValidationError("Incorrect Credentials")
        self.context.update({'user': user})
        return user
    # def validate(self, attrs):
    #     username = attrs.get('username')
    #     password = attrs.get('password')
    #
    #     user = authenticate(username=username, password=password)
    #     if not user or not user.is_active:
    #         raise serializers.ValidationError('Invalid username or password.')
    #
    #     attrs['user'] = user
    #     return attrs
