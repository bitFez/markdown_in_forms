from django.urls import path

from . import views
app_name = 'posts'

urlpatterns = [
    path('', views.home, name='home'),
    path('create_post/', views.submit_post, name='create_post'), # Adding a post
]
