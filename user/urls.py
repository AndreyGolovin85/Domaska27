from django.urls import path

from user.views import UserCreateView, UserListView, UserDeleteView, UserUpdateView, UserDetailView

urlpatterns = [
    path('create/', UserCreateView.as_view()),
    path('', UserListView.as_view()),
    path('delete/<int:pk>/', UserDeleteView.as_view()),
    path('update/<int:pk>/', UserUpdateView.as_view()),
    path('<int:pk>/', UserDetailView.as_view())
]
