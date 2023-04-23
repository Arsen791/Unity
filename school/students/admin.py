from django.contrib import admin
from students.models import User_name, User_birth, User_info, User_work

# Register your models here.
admin.site.register(User_name)
admin.site.register(User_birth)
admin.site.register(User_info)
admin.site.register(User_work)

