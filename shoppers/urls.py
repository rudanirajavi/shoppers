"""
URL configuration for shoppers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from adminside.views import *
from userside.views import *

urlpatterns = [
    path('login/',login),
    path('',user_login),
    path('register/',register),
    path('dashboard/',dashboard),
    path('addadmin/',addadmin),
    path('edit_profile/<int:edit_id>',edit_profile),
    path('adminuserdata/',adminuserdata),
    path('logout/',logout),
    path('home/',home),


    path('slider/',slider),
    path('view_slider/',view_slider),
    path('delete_slide/<int:del_id2>',delete_slide),
    path('edit_slide/<int:edit_id2>',edit_slide),


    path('catagory/<int:cat_id>/', catagory),
    path('add_categorie/',add_categorie),
    path('view_categorie/',view_categorie),
    path('delete_categorie/<int:del_id3>',delete_categorie),
    path('edit_categorie/<int:edit_id3>',edit_categorie),


    path('cart/',cart),
    path('add_cart/<int:prod_id>',add_cart_func),
    path('add_like/<int:prod_id>',add_like),
    path('like',like),
   
    path('delete_cart/<int:del_id5>',delete_cart),
    path('delete_review/<int:del_id6>',delete_review),
    path('delete_like/<int:del_id7>',delete_like),
    path('edit_cart/<int:edit_id5>',edit_cart),

    path('checkout/',checkout),
    path('product_detail/<int:product_id>/',product_detail),
    
    path('contact/',contactpage),
    path('view_contact/',view_contact),

    path('shop/',shop),
    # path('product/<int:product_id>/',product),

    path('add_product/',add_product),
    path('view_product/',view_product),
    path('view_comment/',view_comment),
    path('edit_product/<int:edit_id4>',edit_product),
    path('delete_product/<int:del_id4>',delete_product),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)