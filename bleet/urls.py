from django.urls import path
from .views import (
    BleetListView,
    BleetDetailView,
    BleetCreateView,
    BleetUpdateView,
    BleetDeleteView,
    UserBleetListView,
    FollowsListView,
    FollowersListView)

urlpatterns = [
    path('', BleetListView.as_view(), name='bleet-home'),
    path('bleet/new/', BleetCreateView.as_view(), name='bleet-create'),
    path('bleet/<int:pk>/', BleetDetailView.as_view(), name='bleet-detail'),
    path('user/<str:username>', UserBleetListView.as_view(), name='user-bleets'),
    path('bleet/<int:pk>/update/', BleetUpdateView.as_view(), name='bleet-update'),
    path('bleet/<int:pk>/del/', BleetDeleteView.as_view(), name='bleet-delete'),
    path('user/<str:username>/follows', FollowsListView.as_view(), name='user-follows'),
    path('user/<str:username>/followers', FollowersListView.as_view(), name='user-followers'),
]
