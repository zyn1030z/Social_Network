from django.urls import path
from users import views as users_views
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
]
