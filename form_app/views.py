from django.views.generic import CreateView, ListView

from form_app.forms import UserRegistrationForm
from form_app.models import User


class UsersView(ListView):
    model = User
    context_object_name = "users"
    template_name = "form_app/user_list.html"


class RegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = "form_app/user_create.html"
