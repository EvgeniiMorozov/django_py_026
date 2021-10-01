from django.urls import path

from form_app.views import RegistrationView, UsersView, UserDetail

app_name = "form_app"

urlpatterns = [
    path("", UsersView.as_view(), name="users"),
    path("register", RegistrationView.as_view(), name="register"),
    path("user_detail/<slug:user_slug>", UserDetail.as_view(), name="user_detail")
]
