from django.urls import re_path, path 
from . import views

app_name = "users"


urlpatterns = [
   	# Login
    re_path(r'^login/$', views.LoginView.as_view(), name="login_url"),
    re_path(r'^register/$', views.RegisterView.as_view(), name="register_url"),
    re_path(r'^forgot_password/$', views.ForgotPasswordView.as_view(), name="forgot_password_url"),
    re_path(r'^logout/$', views.LogoutView.as_view(), name="logout_url"),



    re_path(r'^charts/$', views.ChartsView.as_view(), name="charts_url"),

    re_path(r'^tables/$', views.ChartsView.as_view(), name="tables_url"),

]