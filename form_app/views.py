from django.views.generic import CreateView, DetailView, ListView

from form_app.forms import UserRegistrationForm
from form_app.models import User


class UsersView(ListView):
    model = User
    context_object_name = "users"
    template_name = "form_app/user_list.html"


# Переопределив метод get_context_data и назначив success_url = "register/", удалось сделать добавление и отображение
# юзеров на одной странице
class RegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = "form_app/user_create.html"
    success_url = "register/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = User.objects.all()
        return context


class UserDetail(DetailView):
    model = User
    context_object_name = "user"
    slug_url_kwarg = "user_slug"
