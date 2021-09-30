from django.contrib import admin

from form_app.models import User


class UserAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("first_name", "last_name")}


admin.site.register(User, UserAdmin)
