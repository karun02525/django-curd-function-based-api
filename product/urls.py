from django.urls import path
from .views import product,add_product,products,update_product,delete_product,get_books

urlpatterns = [
    path('product',product, name='product'),
    path('products',products,name='product'),
    path('add-product',add_product,name='Add Product'),
    path('update-product/<id>',update_product,name='Update Product'),
    path('delete-product/<id>',delete_product,name='Delete Product'),
    path('get-book',get_books,name='Get Book'),
]
