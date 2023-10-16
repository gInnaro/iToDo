from django.contrib import admin
from .models import Category, Note, Main


admin.site.register(Main)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "authors")


admin.site.register(Category, CategoryAdmin)

class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "authors")


admin.site.register(Note, NoteAdmin)
