from django.urls import path

from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/<str:username>/', views.profile_view, name='profile_view'),
    path('profile/<str:username>/posts/', views.user_posts, name='profile_posts'),
    # path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('follow/<str:username>/', views.follow_user, name='follow_user'),
    # path('unfollow/<str:username>/', views.unfollow_user, name='unfollow_user'),
]
