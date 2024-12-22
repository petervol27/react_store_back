from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_products, name="get_all_products"),
    # path("add_base", views.create_base_products, name="create_products"),
]
