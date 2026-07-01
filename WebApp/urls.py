from django.urls import path
from WebApp import views
urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('product_page/',views.product_page,name="product_page"),
    path('about_page/', views.about_page, name="about_page"),
    path('contact_page/', views.contact_page, name="contact_page"),
    path('filtered_product/<cat_name>', views.filtered_product, name="filtered_product"),
    path('single_item/<int:pro_id>',views.single_item,name="single_item"),
    path('cartpage/',views.cartpage,name="cartpage"),
    path('checkoutpage/', views.checkoutpage, name="checkoutpage"),
    path('contact_save/',views.contact_save,name="contact_save"),

    path('user_registration/',views.user_registration,name="user_registration"),
    path('user_sign_up/',views.user_sign_up,name="user_sign_up"),
    path('user_sign_in/',views.user_sign_in,name="user_sign_in"),
    path('user_logout/', views.user_logout, name="user_logout"),

    path('privacy_policy/', views.privacy_policy, name="privacy_policy"),

    path('save_cart/',views.save_cart,name="save_cart"),
    path('delete_product/<int:c_id>',views.delete_product,name="delete_product"),
    path('cartpage_products/',views.cartpage_products,name="cartpage_products"),

]