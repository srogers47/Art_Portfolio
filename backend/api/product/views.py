from rest_framework import viewsets

from .serializers import ProductSerializer
from .models import Product 
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id') #This can also be name; id is simply a preference.  
    serializer_class = ProductSerializer
