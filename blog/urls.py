
from . import views
from django.urls import path,include
from .views import PostListView,PostdetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView

urlpatterns = [
    path('post/<int:pk>/', PostdetailView.as_view(),name='post-detail'),
    path('', PostListView.as_view(),name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(),name='user-posts'),
    path('new/', PostCreateView.as_view(),name='post-new'),
    path('about/', views.about,name='blog-about'),
    path('post/<int:pk>/update',PostUpdateView.as_view(),name='blog-update'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(),name='blog-delete'),

]
