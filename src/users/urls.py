from django.urls import re_path, path 
from . import views

app_name = "users"


urlpatterns = [
   	# Login
    re_path(r'^login/$', views.LoginView.as_view(), name="login_url"),
    re_path(r'^register/$', views.RegisterView.as_view(), name="register_url"),
    re_path(r'^forgot_password/$', views.ForgotPasswordView.as_view(), name="forgot_password_url"),

]