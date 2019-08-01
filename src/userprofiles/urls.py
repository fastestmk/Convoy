from django.urls import path

from userprofiles.views import (
    change_password,
    edit_profile,
    sign_in,
    sign_out,
    sign_up,
    user_profile,
)

app_name = "Profile"
urlpatterns = [
    path("signup/", sign_up, name="sign_up"),
    path("signin/", sign_in, name="sign_in"),
    path("signout/", sign_out, name="sign_out"),
    path("edit_profile/", edit_profile, name="edit_profile"),
    path("profile/", user_profile, name="profile"),
    path("change_password/", change_password, name="change_password"),
]
