from django.urls import path
from AdminApp import views


urlpatterns = [
    path('loginpage/', views.loginpage, name="loginpage"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('add_category/',views.add_category,name="add_category"),
    path('insert_category/',views.insert_category,name="insert_category"),
    path('view_category/', views.view_category, name="view_category"),
    path('edit_category/<int:t_id>', views.edit_category, name="edit_category"),
    path('update_category/<int:c_id>', views.update_category, name="update_category"),
    path('delete_category/<int:c_id>', views.delete_category, name="delete_category"),

    # path('add_product/',views.add_product,name="add_product"),
    path('view_product/', views.view_product, name="view_product"),
    path('edit_product/<int:pro_id>', views.edit_product, name="edit_product"),
    path('display_product/',views.display_product,name="display_product"),

    path('insert_product/', views.insert_product, name="insert_product"),
    path('new_product/', views.new_product, name="new_product"),
    path('update_product/<int:p_id>', views.update_product, name="update_product"),
    path('delete_product/<int:p_id>', views.delete_product, name="delete_product"),

    path('user_deatils/', views.user_deatils, name="user_deatils"),

]