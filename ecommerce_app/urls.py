from django.contrib import admin
from django.urls import path, include
from . import views
app_name='ecommerce'
urlpatterns = [
    path('',views.index,name='home_page'),

    path('<int:category_id>/',views.cat_pro_list,name='category_product_list'),
    path('product/<int:product_id>/',views.product_detail,name='product_detail_page'),
    path('search/',views.searchresult,name='searchresult'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_page, name='cart_page'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]