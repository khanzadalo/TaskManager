from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'users'
urlpatterns = [
    path('users/login/', views.InLoginView.as_view(), name='login'),
    path('users/logout/', views.OutLogoutView.as_view(next_page='login'), name='logout'),
    path('users/register/', views.RegisterView.as_view(), name='register'),
    path('users/profile/', views.profile_view, name='profile'),
    path('users/profile_edit/', views.ProfileUpdateView.as_view(), name='profile_edit')
]