from django.contrib import admin
from django.urls import path
from .views import index, view_products, create_product, save_product, edit_product, save_edited_product, delete_product


urlpatterns = [
    path('',index, name= 'home-page'),
    path('products',view_products, name= 'products-page'),
    path('new_product',create_product, name= 'new-product-page'),
    path('save_product',save_product, name= 'save-product-page'),
    path('edit_product/<product_id>',edit_product, name= 'edit-product-page'),
    path('save_edited/<edited_product_id>',save_edited_product, name= 'save-after-edit'),
    path('delete_product/<product_id>',delete_product, name= 'delete-product-page'),
]