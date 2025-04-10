from dj_rest_auth.views import LoginView
from dj_rest_auth.views import LogoutView
from django.urls import path

from .views import RegisterUserView, UserListView, UserDetailView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('', UserListView.as_view(), name='user-list'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    # JWT Login and Logout
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
