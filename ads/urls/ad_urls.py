from django.urls import path

from ads.views import AdCreateView, AdDetailView, AdUploadImageView, AdListView

urlpatterns = [
    path('', AdListView.as_view()),
    path('create/', AdCreateView.as_view()),
    path('<int:pk>/', AdDetailView.as_view()),
    path('<int:pk>/apload_image', AdUploadImageView.as_view())
]
