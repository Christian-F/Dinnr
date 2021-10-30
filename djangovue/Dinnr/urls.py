from rest_framework import routers
from django.urls import path, include
from Dinnr import views

router = routers.DefaultRouter()
router.register(r'items', views.FoodItemViewSet) #This maybe 'fooditems'

urlpatterns = [
    path('', include(router.urls)),
]