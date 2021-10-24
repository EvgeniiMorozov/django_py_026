from django.core.cache import cache

from .models import Category


class DataMixin:
    paginate_by = 10

    def get_user_context(self, **kwargs) -> dict:
        context = kwargs

        cats = cache.get("cats")

        if not cats:
            cats = Category.objects.all()
            cache.set("cats", cats, 60)

        context["cats"] = cats
        return context
