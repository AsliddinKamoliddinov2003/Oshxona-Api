from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Category, Product


    
class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name","price", "rating", "slug", "image", "category", "is_active"]
