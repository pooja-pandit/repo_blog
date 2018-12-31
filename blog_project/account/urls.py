from django.urls import path
from account import views
urlpatterns = [
    path('', views.basic, name='basic'),
    path('account/logout/', views.logged_out, name='logged_out'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),

]
