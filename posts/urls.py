from django.urls import path
from .views import PostDetial, PostList, UserList, UserDetail

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/',  UserDetail.as_view()),
    path('<int:pk>/', PostDetial.as_view()),
    path('', PostList.as_view()),
]