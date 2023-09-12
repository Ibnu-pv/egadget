from django.urls import path
from .views import *



urlpatterns = [
    path('cust',CustHomeView.as_view(),name="custhome"),
    path('prodetails/<int:id>',ProductDetailsView.as_view(),name="prdte"),
    path('acart/<int:id>',addcart,name="acart"),
    path('cart',CartListView.as_view(),name="cart"),
    path('rcart/<int:id>',removecart,name="rcart"),
    path('pymnt/<int:id>',PaymentView.as_view(),name="payment"),
    path('order',OrderListView.as_view(),name="order"),
    path('cancelorder/<int:id>',cancelorder,name="corder"),
    # path('log',LogoutView.as_view(),name="logout")
   
    
    
]
