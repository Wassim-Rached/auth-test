from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = Product
		fields = '__all__'

	def create(self, validated_data):
		product = Product.objects.create(**validated_data,owner = self.context['request'].user)
		return product