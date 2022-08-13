from django import views
from django.urls import path
from . import views
from django.conf.urls.static import static  # load img static
from django.conf import settings  # import settings

# 
urlpatterns = [
    path('', views.index, name = 'home'),
    path('products/<slug:data>', views.products_view.as_view(), name='products'),

    #path('products/', views.products, name='products'),
    # path('t_shirt/' , views.shop_category_view.as_view(), name = 't_shirt'),

    path('contact/', views.contact, name='contact'),
    path('checkout/', views.checkout, name='checkout'),
    path('buynow/', views.buynow, name='buynow'),
    path('add-cart/', views.CustomerCartProduct.as_view(), name='CustomerCartProduct'),

    # path('profile_data/', views.profile_data, name='profile_data'),
    path('profile_page/', views.profile_page, name="profile_page"),
    path('profile_update/', views.profile_update, name='profile_update'),

    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),


    path('signup_page/', views.signup_page, name='signup_page'),
    path('signin_page/', views.signin_page, name='signin_page'),
    path('logout/', views.logout, name='logout'),

    path('otp_page/', views.otp_page, name='otp_page'),
    path('otp_verify/', views.otp_verify, name='otp_verify'),
      
    path('Quick_view/<int:pk>', views.Quick_view.as_view(), name='Quick_view'),
    # path('Products_View/<int:pk>', views.Products_View, name='Products_View'),
    path('Customer_cart/',views.Customer_cart, name='Customer_cart'),
    # path('remove_cart/<int:pk>', views.remove_cart, name='remove_cart'),
     # path('product_detail/<int:pk>', views.product_detail_view.as_view(), name='product_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   