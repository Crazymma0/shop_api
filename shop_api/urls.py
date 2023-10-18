from django.contrib import admin
from django.urls import path, include
from product import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/categories/', views.CategoryList.as_view, name='category-list'),
    path('api/v1/categories/<int:pk>/', views.CategoryDetail.as_view, name='category-detail'),
    path('api/v1/products/', views.ProductList.as_view, name='product-list'),
    path('api/v1/products/<int:pk>/', views.ProductDetail.as_view, name='product-detail'),
    path('api/v1/reviews/', views.ReviewList.as_view, name='review-list'),
    path('api/v1/reviews/<int:pk>/', views.ReviewDetail.as_view, name='review-detail'),
]

