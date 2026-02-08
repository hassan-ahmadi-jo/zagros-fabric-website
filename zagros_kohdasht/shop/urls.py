from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('product/', views.product_list_page, name='product_list_page'),
    path('product/filter/<int:id>/', views.product_item_page, name = 'product_item_page'),
    path('categories/', views.categories_page, name='categories_page'),
    path('contact_us/', views.contact_us_page, name='contact_us_page'),
    path('address/', views.address_page, name='address_page'),
]

