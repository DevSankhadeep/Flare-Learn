from django.contrib import admin
from courses.models import Profile, Category, Course


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "bio", "profile_image")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}  # ✅ auto-fill slug in admin
    search_fields = ("name",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "author", "price", "lessons_count", "duration")
    prepopulated_fields = {"slug": ("title",)}  # ✅ auto-fill slug in admin
    search_fields = ("title", "category__name", "author__username")
    list_filter = ("category", "author")
