from .models import Category


class DataMixin:
    paginate_by = 10

    def get_user_context(self, **kwargs) -> dict:
        context = kwargs
        cats = Category.objects.all()
        context["cats"] = cats
        return context
