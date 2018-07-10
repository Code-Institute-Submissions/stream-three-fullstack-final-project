from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AllUser
# Register your models here.

class MyUserAdmin(UserAdmin):
    model = AllUser

    fieldsets = UserAdmin.fieldsets + (
                (None, {'fields':('is_member', 
                                    'is_client', 
                                    'company', 
                                    'phone', 
                                    'position')}),)


admin.site.register(AllUser, MyUserAdmin)





