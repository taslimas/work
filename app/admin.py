from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Role)
@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):

    list_display=['roles']