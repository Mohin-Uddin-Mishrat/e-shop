from rest_framework import serializers
from django.contrib.auth.models import User
from . import models
    
class productSerializer(serializers.ModelSerializer)  :
    class Meta :
        model = models.ProductsModel
        fields = '__all__'

class reviewSerializer(serializers.ModelSerializer)  :
    class Meta :
        model = models.reviewModel
        fields = '__all__'
        
class wishlistSerializer(serializers.ModelSerializer)  :
    class Meta :
        model = models.wishlistModel
        fields = '__all__'