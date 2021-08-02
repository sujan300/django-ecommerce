from django.urls import path
from carts import views


urlpatterns = [
    path('',views.carts,name='carts'),
    path('add_cart/<int:product_id>/',views.add_carts,name='add_cart'),
    path('remove_cart/<int:product_id>/',views.remove_cart,name='remove_cart'),
    path('remove_cart_item/<int:product_id>/',views.remove_cart_item,name='remove_cart_item'),
]