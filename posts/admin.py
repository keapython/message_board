from django.contrib import admin

from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

# or
# admin.site.register(Post)

# or 
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display=('text',)

