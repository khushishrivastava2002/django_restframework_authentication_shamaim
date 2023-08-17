from .views import *
from knox import views as knox_views
from django.urls import path,include

urlpatterns = [
    path('api/register/',RegisterAPI.as_view(),name='register'),
    path('api/login/',LoginAPI.as_view(),name='login'),
    path('api/logout/',knox_views.LogoutView.as_view(),name='logout'),
    path('api/change_password/',ChangePasswordView.as_view(),name='change_password'),
    path('api/password_reset/',include('django_rest_passwordreset.urls',namespace='password_reset')),
    # path('api/change-password/',ChangePasswordView.as_View(),name="change-password")
    # path('api/logoutall',knox_views.LogoutAllView.as_View(),name='logoutall')
]
