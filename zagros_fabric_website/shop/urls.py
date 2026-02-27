from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index_page'),
    path('product/', views.ProductListView.as_view(), name='product_list_page'),
    path('product/filter/<int:id>/', views.ProductItemView.as_view(), name = 'product_item_page'),
    path('categories/', views.CategoriesView.as_view(), name='categories_page'),
    path('contact_us/', views.ContactUsView.as_view(), name='contact_us_page'),
    path('address/', views.AddressView.as_view(), name='address_page'),
]

