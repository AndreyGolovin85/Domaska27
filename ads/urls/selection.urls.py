from django.urls import path

from ads.views import SelectionListView, SelectionDetailSerializer, SelectionDeleteView, SelectionCreateView,\
    SelectionUpdateView

urlpatterns = [
    path('', SelectionListView.as_view()),
    path('<int:pk>/detail/', SelectionDetailSerializer.as_view()),
    path('create/<int:pk>/', SelectionCreateView.as_view()),
    path('update/<int:pk>/', SelectionUpdateView.as_view()),
    path('<int:pk>/delete/', SelectionDeleteView.as_view()),
]
