from django.urls import path
from . import views
urlpatterns = [
    path('<int:post_id>', views.detail, name='detail'),
    path('<int:post_id>/create', views.createreview, name='createreview'),
    path('review/<int:review_id>', views.updatereview, name='updatereview'),
    path('review/<int:review_id>/delete', views.deletereview, name='deletereview'),
    path('posts/new/', views.create_post, name='create_post'),
    path('post/<int:post_id>/update', views.update_post, name='update_post'),
    path('post/<int:post_id>/delete', views.delete_post, name='delete_post'),
]