from django.urls import path, include

from core.views import UserCreateAPIView, UserLoginView, UserDetailUpdateView, UserChangePasswordView

urlpatterns = [
    path('signup', UserCreateAPIView.as_view(), name='user_create'),
    # path('', include('django.contrib.auth.urls')),
    path('login', UserLoginView.as_view(), name='user_login'),
    path('profile', UserDetailUpdateView.as_view(), name='user_detail_update'),
    path('update_password', UserChangePasswordView.as_view(), name='user_change_password'),
]
