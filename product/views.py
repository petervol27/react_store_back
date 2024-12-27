from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated


@api_view(["GET"])
def all_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


# @api_view(["GET"])
# def create_base_products(request):
#     products = [
#         {
#             "name": "Leather Jacket",
#             "price": 120,
#             "image": "https://images.unsplash.com/photo-1521223890158-f9f7c3d5d504?q=80&w=1492&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
#         },
#         {
#             "name": "Wireless Bluetooth Headphones",
#             "price": 89.99,
#             "image": "https://images.unsplash.com/photo-1505739718967-6df30ff369c7?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
#         },
#         {
#             "name": "Luxury Watch",
#             "price": 250,
#             "image": "https://images.unsplash.com/photo-1670404160620-a3a86428560e?q=80&w=1925&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
#         },
#         {
#             "name": "Running Shoes",
#             "price": 75,
#             "image": "https://images.unsplash.com/photo-1460353581641-37baddab0fa2?q=80&w=1742&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
#         },
#         {
#             "name": "Smartphone",
#             "price": 699.99,
#             "image": "https://images.unsplash.com/photo-1598965402089-897ce52e8355?q=80&w=1936&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
#         },
#         {
#             "name": "Backpack",
#             "price": 45,
#             "image": "https://images.unsplash.com/photo-1474376962954-d8a681cc53b2?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
#         },
#         {
#             "name": "Sunglasses",
#             "price": 60,
#             "image": "https://images.unsplash.com/photo-1473496169904-658ba7c44d8a?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
#         },
#     ]
#     serializer = ProductSerializer(data=products, many=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
