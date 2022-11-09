from django.contrib import admin
from .models import TipsPost, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(TipsPost)
class TipsPostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created', 'updated', 'part_of_game', 'author')
    list_display = ('title', 'slug', 'status', 'created', 'part_of_game')
    search_fields = ['title', 'part_of_game']
    summernote_fields = ('stance_content', 'swing_content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created', 'approved')
    list_filter = ('approved', 'created')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
