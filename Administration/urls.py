from django.urls import path
from .views import AdministrationCls

admin_obj = AdministrationCls()
urlpatterns = [
    #----------------------------------------------------------------------
    path('login', admin_obj.login_page,name='login'),
    path('base', admin_obj.base,name='base'),
    path('add_class_page', admin_obj.add_class_page,name='add_class'),
    path('create_class', admin_obj.create_class,name='create_class'),
    path('class_data_page', admin_obj.class_data_page,name='class_data_page'),
    path('edit_class_page', admin_obj.edit_class_page,name='edit_class_page'),
    path('update_class', admin_obj.update_class,name='update_class'),
     path('login', admin_obj.login_page,name='login'),
    path('user_login', admin_obj.user_login,name='user_login'),
    path('not_found', admin_obj.not_found,name='not_found'),
    path('logout', admin_obj.user_log_out,name='logout'),
    path('register_page', admin_obj.register_page,name='register_page'),
    path('register_user', admin_obj.register_user,name='register_user'),
    path('add_book_page', admin_obj.add_book_page,name='add_book_page'),
    path('add_book', admin_obj.add_book,name='add_book'),
    path('book_list_page', admin_obj.book_list_page,name='book_list_page'),
    path('edit_book_page', admin_obj.edit_book_page,name='edit_book_page'),
    path('edit_book', admin_obj.edit_book,name='edit_book'),
    
]
