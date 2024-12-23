from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ShopUserSerializer


@permission_classes(IsAuthenticated)
@api_view(["GET"])
def get_user(request):
    name = request.user.username
    return Response(name)
