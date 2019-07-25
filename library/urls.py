from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls import url
urlpatterns = [
    path('', views.home, name = 'home'),
    path('search/', views.search_book, name = 'search'),
    path('find_order/', views.search_order, name = 'find_order'),
    path('leaderboard/', views.leaderboard, name = 'leaderboard'),
    path('shop/', views.shop, name = 'shop'),
    path('cart/', views.cart, name = 'cart'),
    url(r'^add-to-cart/(?P<item_id>[-\w]+)/$', views.cart_add, name="add_to_cart"),
]
