from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Category, Product, Rate, Comment, Basket, Order, OrderItem
from .serializers import (
    CategorySerializer, ProductSerializer, RateSerializer, CommentSerializer,
    BasketSerializer, OrderSerializer, CreateOrderSerializer, OrderItemSerializer
)
from rest_framework.pagination import PageNumberPagination
from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view
from django.utils.decorators import method_decorator
from rest_framework.filters import SearchFilter

# ----- Pagination Class -----
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10  # Change this to whatever number you want per page
    page_size_query_param = 'page_size'
    max_page_size = 100

# ----- Category Views -----
@method_decorator(cache_page(60 * 15), name='dispatch')  # Cache for 15 minutes
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = StandardResultsSetPagination  # Add pagination
    filter_backends = (SearchFilter,)
    search_fields = ('name',)  # Allow searching by 'name' field

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# ----- Product Views -----
@method_decorator(cache_page(60 * 15), name='dispatch')  # Cache for 15 minutes
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination  # Add pagination
    filter_backends = (SearchFilter,)
    search_fields = ('name',)  # Allow searching by 'name' field

    def get_queryset(self):
        queryset = Product.objects.all()
        # Sorting by price (ascending and descending)
        sort_by_price = self.request.query_params.get('sort_by_price', None)
        if sort_by_price == 'expensive':
            queryset = queryset.order_by('-price')
        elif sort_by_price == 'cheap':
            queryset = queryset.order_by('price')
        return queryset

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# ----- Rate Views -----
class RateListCreateView(generics.ListCreateAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# ----- Comment Views -----
class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# ----- Basket Views -----
class BasketListCreateView(generics.ListCreateAPIView):
    serializer_class = BasketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Basket.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BasketDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BasketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Basket.objects.filter(user=self.request.user)

# ----- Order Views -----
class CreateOrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = CreateOrderSerializer
    permission_classes = [IsAuthenticated]

class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class OrderDetailView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
