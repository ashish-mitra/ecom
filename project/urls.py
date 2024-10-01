"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home" ),
    path('about/', views.about, name="about" ),

    path('login/', views.login_user , name="login" ),
    path('logout/', views.logout_user , name="logout" ),
    path('signup/', views.signup_user , name="signup" ),
    path('profile/', views.profile, name='profile'),

    path('search/', views.search_paintings , name="search_paintings" ),

    path('base/', views.base, name="base" ),

    path('product/<int:pk>/', views.product, name="product" ),

    path('category/<str:cat>/', views.category, name="category" ),

    path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/<int:painting_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),

    path('checkout/', views.checkout, name='checkout'),
    path('order_confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
    path('orders/', views.view_orders, name='view_orders'),
    
]+ static(settings. MEDIA_URL, document_root=settings.MEDIA_ROOT)

