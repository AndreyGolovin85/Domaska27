from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user.views import UserCreateView, UserListView, UserDeleteView, UserUpdateView, UserDetailView, LocationViewSet


urlpatterns = [
    path('', UserListView.as_view()),
    path('<int:pk>/delete/', UserDeleteView.as_view()),
    path('update/<int:pk>/', UserUpdateView.as_view()),
    path('create/<int:pk>/', UserCreateView.as_view()),
    path('<int:pk>/', UserDetailView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
