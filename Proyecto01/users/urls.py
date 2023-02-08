from django.urls import path
from users.views import login_view, signup_view, update_user_profile, profile_view
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', login_view, name = 'login'),
    path('logout/', LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),
    path('signup/', signup_view, name = 'signup'),
    path('update_profile/', update_user_profile, name='update profile'),
    path('profile/', profile_view, name='profile'),
]