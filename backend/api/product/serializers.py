from rest_framework import serializers

from .models import Product 

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    #See docs this is pretty much boilerplate.  
    #Need to specify None max_length or else url won't format properly (won't be full URL).
    image = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=True, required=False) 
    class Meta:
        Model = Product
        fields = ('id', 'name', 'description', 'price', 'image', 'category')
