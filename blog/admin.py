from django.contrib import admin
from .models import Blog, AttachedImage, Category, Comment

class InlineImage(admin.TabularInline):
    model = AttachedImage
    extra = 2

class BlogAdmin(admin.ModelAdmin):
    inlines = [InlineImage]

admin.site.register(Blog, BlogAdmin)

admin.site.register(Category)
admin.site.register(Comment)