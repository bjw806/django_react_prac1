from .views import PostList, PostDetail, PostListDetailfilter, CreatePost, EditPost, AdminPostDetail, DeletePost, \
    LoginAccount
from django.urls import path

app_name = 'blog_api'

urlpatterns = [
    path('', PostList.as_view(), name='listpost'),
    path('user/', LoginAccount.as_view(), name='loginaccount'),
    path('post/<str:pk>/', PostDetail.as_view(), name='detailpost'),
    path('search/', PostListDetailfilter.as_view(), name='searchpost'),
    path('admin/create/', CreatePost.as_view(), name='createpost'),
    path('admin/edit/postdetail/<int:pk>/', AdminPostDetail.as_view(), name='admindetailpost'),
    path('admin/edit/<int:pk>/', EditPost.as_view(), name='editpost'),
    path('admin/delete/<int:pk>/', DeletePost.as_view(), name='deletepost'),
]
