from django.urls import path

from user.views import UserCreateView, UserListView, UserDeleteView, UserUpdateView, UserDetailView, LocationViewSet


urlpatterns = [
    path('', UserListView.as_view()),
    path('delete/', UserDeleteView.as_view()),
    path('update/<int:pk>/', UserUpdateView.as_view()),
    path('create/<int:pk>/', UserCreateView.as_view()),
    path('<int:pk>/', UserDetailView.as_view())
]
