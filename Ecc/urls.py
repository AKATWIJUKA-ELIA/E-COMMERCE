from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
      path('verify/', views.verify_signature,name='verify'),
    path('', views.userpage,name='userpage'),
    path('service/', views.service,name="service"),
    path('contacts/', views.contacts,name="contact"),
    path('about/', views.about,name="about"),
    path('gallery/',views.gallery,name='gallery'),
    path('get-gallery/',views.get_gallery,name='get-gallery'),
    path('sign_up/', views.sign_up,name="sign_up"),
    path('sign_in/', views.sign_in,name="sign_in"),
    path('reset/', views.ForgotPassword,name="reset"),
    path('reset-password',views.ChangePassword, name="reset-password"),
    path('log_out/', views.log_out,name="log_out"),
    path('home/', views.userpage,name="userpage"),
    path('profile/', views.profile,name="profile"),
    path('admin_profile/', views.admin_profile,name="admin_profile"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('admini/', views.admin,name="admin"),
    path('admin-login/', views.admin_login,name="admin-login"),
    path('admin-signup/', views.admin_signup,name="admin_signup"),
    path('delete/', views.delete,name="delete"),# Deleting Products
    path('update/', views.update,name="update"), # updating products
    path('delete_from_cart/', views.delete_from_cart,name="delete_from_cart"),
    path('cart/', views.cart,name="cart"),
    path('checkout/', views.check_out,name="check_out"),
    path('increase_quantity/', views.increase,name="increase_quantity"),
    path('decrease_quantity/', views.decrease,name="decrease_quantity"),
    path('newsletter/', views.news_letter,name="news_letter"),
    path('Add_Item_to_cart/', views.Add_Item_to_cart,name="Add_Item_to_cart"),
    path('payments/', views.payments,name="payments"),
    path('Send_email/', views.Send_email,name="Send_email"),
    path('product/<str:pk>/', views.detail, name='detail'),
    path('sell/', views.Sell,name='sell'),
    path('search/', views.search_view, name='search'),
    path("footer/",views.footer,name="footer"),
    path("approve/",views.approve,name='approve'),
    path("category-add/",views.Add_Category,name='Add_Category'),

]
if settings.DEBUG:
      urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
