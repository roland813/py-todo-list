from django.contrib import admin
from tags.models import Tag, Task


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass
