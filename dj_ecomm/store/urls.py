from django.urls import path
from .views import (
    HomeView,
    OrderSummaryView,
    ItemDetailView,
    add_to_cart,
    remove_from_cart,
    
    remove_single_item_from_cart,
    
    CheckoutView,
    AddCouponView,
    PaymentView,
    RequestRefundView
)

app_name = 'store'
urlpatterns = [
    path('', HomeView.as_view(), name='home'), #UNDERSTOOD
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    
    # Following used by order_summary.html
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    
    path('request-refund/', RequestRefundView.as_view(), name='request-refund')
]
