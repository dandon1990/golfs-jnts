from . import views
from django.urls import path


urlpatterns = [
    path('', views.TipsPostList.as_view(), name='home'),
    path('<slug:slug>/', views.TipsPostDetail.as_view(), name='post_detail'),
    path(
        'post/<slug:slug>/',
        views.CreateCommentView.as_view(),
        name='post_comment'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('edit/<int:comment_id>/', views.EditComment.as_view(), name='edit'),
    path(
        'delete/<int:comment_id>/',
        views.DeleteComment.as_view(),
        name='delete')
]
