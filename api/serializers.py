from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	email = serializers.EmailField(required=True,max_length=254)
	username = serializers.CharField(required=True,max_length=254)
	password = serializers.CharField(required=True, write_only=True)

	class Meta:
		model = User
		fields = ('id', 'username', 'email', 'password')
		extra_kwargs = {'password': {'write_only': True}}

	def validate(self, args):
		email = args.get('email')
		username = args.get('username')
		if User.objects.filter(email=email).exists():
			raise serializers.ValidationError('Email already exists')
		if User.objects.filter(username=username).exists():
			raise serializers.ValidationError('Username already exists')
		return super().validate(args)	

	def create(self, validated_data):
		return User.objects.create_user(**validated_data)
