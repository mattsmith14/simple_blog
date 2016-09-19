from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'get_absolute_url')

admin.site.register(Post, PostAdmin)
