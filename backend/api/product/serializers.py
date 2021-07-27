from rest_framework import serializers

from .models import Product 

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty=False, required=False) #See docs this is pretty much boilerplate.  Need to specify None max_length or else url won't format properly (won't be full URL).
    class Meta:
        Model = Product
        fields = ('id', 'name', 'description', 'price', 'image', 'category')
