from django.contrib import admin
from .models import*
from django.contrib.auth.admin import UserAdmin
class UserModel(UserAdmin):
    list_display=['username','user_type']
admin.site.register(CustomUser,UserModel)
admin.site.register(Course)
admin.site.register(Session)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Subject)
admin.site.register(Staff_notification)
admin.site.register(Staff_leave)

# Register your models here.
