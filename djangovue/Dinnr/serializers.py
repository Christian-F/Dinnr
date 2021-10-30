from rest_framework import serializers
from Dinnr.models import FoodItem

class FoodItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, allow_blank=False)
    brand_name = serializers.CharField(max_length=100, allow_blank=False)
    
    class Meta:
        model = FoodItem
        fields = ['name','brand_name']