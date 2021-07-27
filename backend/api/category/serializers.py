from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.HyperlinkedModelSerializer): #Search stackoverflow for context. documentation for serialization has steep learning curve, but is also is worth reading
    class Meta:
        model = Category
        fields = ('name', 'description') #need 'fields' NOT 'field' 
