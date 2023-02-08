from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
#
class ProductListCreateAPIView(ListCreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#
class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	permission_classes = [permissions.IsAdminUser | IsOwnerOrReadOnly]

class MyProducts(APIView):
	permission_classes=[permissions.IsAuthenticated]
	def get(self,request,format=None):
                products = Product.objects.filter(owner=request.user)
                serializer = ProductSerializer(products,many=True)
                return Response(serializer.data)