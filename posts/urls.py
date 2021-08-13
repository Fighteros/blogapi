from django.urls import path
from .views import PostDetial, PostList

urlpatterns = [
    path('<int:pk>/', PostDetial.as_view()),
    path('', PostList.as_view())
]