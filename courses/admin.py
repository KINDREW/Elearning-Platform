from django.contrib import admin
from .models import Course, Module, Subject
# Register your models here.


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("title", "slug",)
    list_filter = ("title",)
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}


class ModuleInline(admin.StackedInline):
    model = Module


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("courses", "title", "description")
    list_filter = ("title",)
    search_fields = ["title"]


@admin.register(Course)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ("owner", "subject", "title", "created")
    list_filter = ("created", "subject")
    search_fields = ["title", "overview"]
    prepopulated_fields = {"slug": ("title",)}
    inline = [ModuleInline]


admin.site.index_template = 'memcache_status/admin_index.html'
