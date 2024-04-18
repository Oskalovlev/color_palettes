from django.contrib import admin

from user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "middle_name",
        "username",
    )
    search_fields = ("first_name", "username")
    list_filter = ("first_name", "username")
    empty_value_display = "--пусто--"
