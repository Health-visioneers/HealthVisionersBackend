from django.urls import path
from .views import UserSignup, UserLoginView , UserLogoutView , userhome
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/<str:user_type>/', UserSignup, name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', userhome , name='home'),
    # other urls...
]