"""TMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path , include
from app.views import *
from app import views as app_view
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('index', index, name="index"),
    path('', include("django.contrib.auth.urls")),
    path('staff',staff,name='staff'),
    path('staff/detail/<int:pk>/',staff_detail,name='staff-detail'),
    path('products',products,name='products'),
    path('products/delete/<int:pk>/',product_delete,name='products-delete'),
    path('products/edit/<int:pk>/',product_edit,name='products-edit'),
    path('order',order,name='order'),
    path("khaltirequest/", khaltirequest, name="khaltirequest"),
    path("khaltiverify/", khaltiverify, name="khaltiverify"),
    path('register',register,name='register'),
    path('profile',profile,name='profile'),
    path('',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
   
    
    
    
   
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

  