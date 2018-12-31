from django.contrib import admin

from blog.models import Blog,Category,Topic,Comment
from django_summernote.admin import SummernoteModelAdmin


class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = ('details',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Topic)
admin.site.register(Category)
admin.site.register(Comment)

