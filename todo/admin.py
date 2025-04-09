from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Task, Tag

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("date_of_birth",)
    fieldsets = UserAdmin.fieldsets + (
        ("Personal info", {"fields": ("date_of_birth",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Personal info", {
            "fields": ("first_name", "last_name", "date_of_birth"),
        }),
    )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("content", "created_at", "deadline", "is_done")
    search_fields = ("content",)
    list_filter = ("is_done", "deadline")
    ordering = ("-created_at",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
