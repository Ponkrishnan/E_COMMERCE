from django.urls import path
from .views import *

urlpatterns=[
    path('',index,name='index'),
    path('shop',shop,name='shop'),
    path('detail',detail,name='detail'),
    path('contact',contact,name='contact'),
    path('checkout',checkout,name='checkout'),
    path('cart',cart,name='cart'),
]

