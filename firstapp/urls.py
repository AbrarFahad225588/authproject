from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login_user,name='login'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.logout_user,name='logout'),
    path('change_password/',views.change_password,name='change_password'),
    
]
