from django.contrib import admin
from . models import Blog_Table,Comment,Profile

# Register your models here.
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
admin.site.register(Blog_Table,BlogModelAdmin)
admin.site.register(Comment)
admin.site.register(Profile)