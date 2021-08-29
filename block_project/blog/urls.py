from django.urls import path
from .views import BlogPageView, BlogDetailView, BlogCreateView


urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='detailView'),
    path('', BlogPageView.as_view(), name='home'),
    path('post/new/', BlogCreateView.as_view(), name='new_post')

]