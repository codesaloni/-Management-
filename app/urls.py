from django.urls import path
from .views import*

urlpatterns = [
    path('home/',home,name="home"),
    path('product/',product,name="product"),
    path('product/delete/<int:pk>/', product_delete, name='deleteitem'),
    path('product/update/<int:pk>/', update_product, name='update_product'),
    path('staf/',staf,name='staf'),
    path('staff/delete/<int:pk>/',staffadd_delete,name='staffdelete'),
    path('staff/update/<int:pk>/', update_staff, name='update_staff'),
    path('login/',login,name="login"),
    path('staffadd/',staffadd,name="staffadd"),
    path('productadd/',productadd,name="productadd"),
    path('seller/',seller,name='seller'),
    path('seller/delete/<int:pk>/',seller_delete,name='sellerdelete'),
    path('seller/update/<int:pk>/', update_seller, name='update_seller'),
    path('selleradd/',selleradd,name='selleradd'),
    path('signup/',signup,name="sin"),

    
  
    
]