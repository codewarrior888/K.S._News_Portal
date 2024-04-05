from django.contrib import admin
from .models import Author, Category, Post, Comment, PostCategory


class CategoryInline(admin.TabularInline):
    model = PostCategory
    extra = 1


class PostAdmin(admin.ModelAdmin):
    model = Post, Category
    inlines = (CategoryInline,)
    # list_display = ('post_genre', 'post_time')
    list_filter = ('category', 'author')
    search_fields = ('post_title', 'category__name')


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(PostCategory)