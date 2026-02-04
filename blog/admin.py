from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("body", "author", "post", "created_on", "approved")
    list_filter = ("approved", "created_on")
    search_fields = ("author__username", "body", "post__title")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)



