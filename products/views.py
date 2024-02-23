from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import viewsets
from rest_framework import  filters
from django_filters.rest_framework import DjangoFilterBackend

class productView(viewsets.ModelViewSet):
    queryset = models.ProductsModel.objects.all()
    serializer_class =serializers.productSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['size','color']
    ordering_fields = ['price']


class reviewViewset(viewsets.ModelViewSet):
    queryset = models.reviewModel.objects.all()
    serializer_class =serializers.reviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product']


    


class wishlistViewset(viewsets.ModelViewSet):
    queryset = models.wishlistModel.objects.all()
    serializer_class =serializers.wishlistSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']



