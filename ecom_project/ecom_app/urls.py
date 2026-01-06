"""
URL configuration for ecom_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from ecom_app import views as v

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('' ,v.home , name = 'index'),
    

    path('login/',v.user_login,name="login"),
    path('register/',v.user_register,name="register"),
    path('logout/', v.user_logout, name='logout'),
    path('product_details/<int:pid>', v.product_details, name="product_details"),
    path('addtocart/<int:pid>/',v.addtocart, name='addtocart'),
    path('cart/',v.cartt, name='cartt'),
    path('updateqty/<qv>/<cid>/',v.updateqty, name="updateqty"),
    path('removepc/<cid>',v.removepc, name="removepc"),
    path('placeorder/',v.placeorder,name='placeorder'),
    path('pay/',v.pay, name='pay'),
    path('add-ingredient/', v.add_ingredient, name='add_ingredient'),
    

 
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)