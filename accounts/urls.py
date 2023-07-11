from django.urls import path
from . import views

urlpatterns = [
    path('signupaccount/', views.signupaccount, name='signupaccount'),
    path('logout/', views.logoutaccount, name='logoutaccount'),
    path('login/', views.loginaccount, name='loginaccount'),
    # path('profile/', views.view_profile, name='view_profile'),
    path('profile/<int:user_id>/', views.view_profile, name='view_profile'),
]