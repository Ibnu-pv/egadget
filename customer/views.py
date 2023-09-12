from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View,ListView,DetailView
from account.models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

def signin_required(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            messages.error(request,"please Login first!!")
            return redirect("h")
    return inner  
desc=[never_cache,signin_required]  





# Create your views here.

# class CustHomeView(View):
#     def get(self,request):
#         res=Products.objects.all()
#         return render(request,"cusHome.html",{"data":res})
@method_decorator(desc,name='dispatch')
class CustHomeView(ListView):
    template_name="custHome.html"
    queryset=Products.objects.all()
    context_object_name="products"
    
    
# class ProductDetailsView(View):
#     def get(self,request,**kwargs):
#         pid=kwargs.get('id')
#         pro=Products.objects.get(id=pid)
#         return render(request,"product details.html",{"data":pro}) 

@method_decorator(desc,name='dispatch')
class ProductDetailsView(DetailView):
    template_name="Product details.html"
    pk_url_kwarg='id'
    queryset=Products.objects.all()
    context_object_name='data'
    
@method_decorator(desc,name='dispatch')    
class CartListView(ListView):
     template_name="cart.html"   
     queryset=Cart.objects.all()
     context_object_name="cart"
     def get_queryset(self):
         return Cart.objects.filter(user=self.request.user,status='cart')
    
    
desc  
def addcart(request,*args,**kwargs):
    id=kwargs.get("id")
    pro=Products.objects.get(id=id)
    user=request.user
    qty=request.POST.get('qnt')
    Cart.objects.create(products=pro,user=user,quantity=qty)
    messages.success(request,"Added to cart")
    return redirect('custhome')

desc
def removecart(request,**kwargs):
    pid=kwargs.get("id")
    c=Cart.objects.get(id=pid)
    c.delete()
    messages.success(request,"cart item removed")
    return redirect('cart')

@method_decorator(desc,name='dispatch')
class PaymentView(TemplateView):
    template_name="payment.html"
    
    def post(self,request,*args,**kwargs):
        cid=kwargs.get("id")
        cart=Cart.objects.get(id=cid)
        ad=request.POST.get("address")
        ph=request.POST.get("phone")
        Order.objects.create(cart=cart,address=ad,phone=ph)
        cart.status="Order placed"
        cart.save()
        messages.success(request,"order placed successfull ")
        return redirect("cart")
    
@method_decorator(desc,name='dispatch')    
class OrderListView(ListView):
    template_name="order.html" 
    queryset=Order.objects.all()
    context_object_name="order"   
    
    def get_queryset(self):
        return Order.objects.filter(cart__user=self.request.user)
    
desc  
def cancelorder(request,*args,**kwargs):
    oid=kwargs.get("id")
    order=Order.objects.get(id=oid)
    order.status='Cancelled'
    order.save()
    messages.success(request,"Order cancelled")    
    return redirect('order')




    
    
    
        
    
    

    
    


   
    
