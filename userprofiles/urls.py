from django.urls import path

from userprofiles.views import sign_up, sign_in, sign_out, edit_profile, user_profile, change_password

app_name = 'Profile'
urlpatterns = [
    path('signup/', sign_up, name='sign_up'),
    path('signin/', sign_in, name='sign_in'),
    path('signout/', sign_out, name='sign_out'),
    path('edit_profile/', edit_profile, name="edit_profile"),
    path('profile/', user_profile, name="profile"),
    path('change_password/', change_password, name="change_password"),
]
