from django.contrib import admin
from.models import Post

# Register your models here.

#this adds Posts to the Django admin page
admin.site.register(Post)
