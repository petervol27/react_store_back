from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Cart, CartItem
from .serializers import CartItemSerializer, CartSerializer
from product.models import Product
from product.serializers import ProductSerializer


@permission_classes(IsAuthenticated)
@api_view(["GET"])
def get_cart(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    products = []
    for item in cart_items:
        product = Product.objects.get(id=item.product.id)
        products.append(product)
    serializer_cart = CartItemSerializer(cart_items, many=True)
    serializer_products = ProductSerializer(products, many=True)
    serializers = {
        "cart_items": serializer_cart.data,
        "products": serializer_products.data,
    }
    return Response(serializers)


@permission_classes(IsAuthenticated)
@api_view(["POST"])
def add_to_cart(request):
    cart = Cart.objects.get(user=request.user)
    product = Product.objects.get(id=request.data["id"])
    try:
        cart_item = CartItem.objects.get(product_id=product.id)
        print(cart_item)
        print(cart_item.quantity)
        cart_item.quantity += 1
        cart_item.save()
        print(cart_item.quantity)
        return Response("added succesfully")

    except:
        cart_item = CartItem.objects.create(product=product, cart=cart)
        print("except")
        print(cart_item)
        serializer = CartItemSerializer(data=cart_item)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
