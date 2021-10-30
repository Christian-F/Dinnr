from rest_framework import viewsets
from Dinnr.models import FoodItem
from Dinnr.serializers import FoodItemSerializer

# Create your views here.
class FoodItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows food items to be viewed or edited.
    """
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer