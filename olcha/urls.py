from django.urls import path
from .views import (
    CategoryListCreateView, CategoryDetailView,
    ProductListCreateView, ProductDetailView,
    RateListCreateView, CommentListCreateView,
    BasketListCreateView, BasketDetailView,
    CreateOrderView, OrderListView, OrderDetailView
)

urlpatterns = [
    # Categories
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

    # Products
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    # Ratings
    path('ratings/', RateListCreateView.as_view(), name='rating-list'),

    # Comments
    path('comments/', CommentListCreateView.as_view(), name='comment-list'),

    # Basket
    path('basket/', BasketListCreateView.as_view(), name='basket-list'),
    path('basket/<int:pk>/', BasketDetailView.as_view(), name='basket-detail'),

    # Orders
    path('orders/create/', CreateOrderView.as_view(), name='create-order'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
]
