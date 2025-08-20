from django.contrib import admin
from .models import Video, Comment, Favorite

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    readonly_fields = ('user', 'text', 'is_shared', 'created_at')
    can_delete = False

class FavoriteInline(admin.TabularInline):
    model = Favorite
    extra = 0
    readonly_fields = ('user', 'is_favorite', 'created_at')
    can_delete = False

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_by', 'uploaded_at')
    list_filter = ('uploaded_at', 'uploaded_by')
    search_fields = ('title', 'description', 'uploaded_by__username')
    inlines = [CommentInline, FavoriteInline]
    readonly_fields = ('uploaded_at',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'video', 'is_shared', 'created_at')
    list_filter = ('is_shared', 'created_at', 'video', 'user')
    search_fields = ('text', 'user__username', 'video__title')
    readonly_fields = ('created_at',)

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'video', 'is_favorite', 'created_at')
    list_filter = ('is_favorite', 'created_at', 'video', 'user')
    search_fields = ('user__username', 'video__title')
    readonly_fields = ('created_at',)

