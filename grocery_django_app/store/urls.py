from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.grocery_home, name='grocery_home'),
    path('vegetables/', views.vegetables, name='vegetables'),
    path('fruits/', views.fruits, name='fruits'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('payment/', views.payment, name='payment'),
    path('success/', views.success, name='success'),
    path('failure/', views.failure, name='failure'),
    path('logout/', views.logout_view, name='logout'),
]
