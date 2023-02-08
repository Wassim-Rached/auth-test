from django.urls import path
from . import views


urlpatterns = [
	path('<int:pk>/', views.ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
	path('', views.ProductListCreateAPIView.as_view(), name='product-list'),
	path('mine/',views.MyProducts.as_view(), name='my-products'),
]