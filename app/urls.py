from django.urls import path
from . import views

from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('product/', views.ProductListView.as_view(), name='product'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('search/', views.search, name='search'),
]
