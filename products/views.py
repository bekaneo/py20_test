from products.models import Product
from .serializers import ProductListSerializer, ProductSerializer
from rest_framework.generics import (ListAPIView, CreateAPIView,
                                     UpdateAPIView, RetrieveAPIView,
                                     DestroyAPIView, ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from rest_framework.viewsets import ModelViewSet
from products.filters import ProductPriceFilter


# @api_view(['GET'])
# def products_list(request):
#     products = Product.objects.all()
#     # products = Product.objects.filter()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)


# class ProductsListView(APIView):
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)


class ProductsListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductDetailsView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CreateProductView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UpdateProductView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class DeleteProductView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    filterset_class = ProductPriceFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return super().get_serializer_class()

# post -> create
# get -> list, retrieve
# put, patch -> full or partial update
# delete -> destroy
