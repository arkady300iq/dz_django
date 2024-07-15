from django.urls import path 
from myapp import views

urlpatterns = [
    path("", views.product_list, name = "product-list"),
    path("product-details/<int:pk>/", views.product_details, name = "product-details"),
]

