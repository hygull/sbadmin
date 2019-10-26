from django.urls import re_path, path 
from . import views

app_name = "users"


urlpatterns = [
   	# Login
    re_path(r'^$', views.LoginView.as_view(), name="login_url"),
    re_path(r'^$', views.RegisterView.as_view(), name="register_url"),
]