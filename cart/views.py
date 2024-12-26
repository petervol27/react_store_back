from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Cart, CartItem
from .serializers import CartItemSerializer, CartSerializer
from product.models import Product


@permission_classes(IsAuthenticated)
@api_view(["GET"])
def get_cart(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    serializer = CartItemSerializer(cart_items, many=True)
    return Response(serializer.data)


@permission_classes(IsAuthenticated)
@api_view(["POST"])
def add_to_cart(request):
    cart = Cart.objects.get(user=request.user)
    product = Product.objects.get(id=request.data["id"])
    try:
        cart_item = CartItem.objects.get(product_id=product.id)
        cart_item.quantity + 1
        return Response(serializer.data)

    except:
        cart_item = CartItem.objects.create(product=product, cart=cart)
        serializer = CartItemSerializer(data=cart_item)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
