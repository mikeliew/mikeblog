from django.contrib import admin

from .models import Post, Category, Comment

class CommentItemInline(admin.TabularInline):
	model = Comment
	raw_id_fields = ['post']

class PostAdmin(admin.ModelAdmin):
	search_fields = ['title', 'intro', 'body']
	list_display = ['title', 'slug', 'category', 'status', 'created_date']
	list_filter = ['category', 'created_date', 'status']
	prepopulated_fields = {'slug': ('title',)}
	inlines = [CommentItemInline]

class CategoryAdmin(admin.ModelAdmin):
	search_fields = ['title']
	list_display = ['title']
	prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'created_at']

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
