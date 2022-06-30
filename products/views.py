from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product
from .serializers import ProductSerializer


@api_view(['GET'])
def products_list(request):
    products = Product.objects.all()
    # products = Product.objects.filter()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
