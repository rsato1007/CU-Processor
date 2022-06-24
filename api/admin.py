from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Member

# When utilizing abstract user, you'll need to add the following code for the extra fields
# to show up in Django's admin panel.
fields = list(UserAdmin.fieldsets)
fields[0] = (None, {'fields': ('username', 'password', 'staff_level')})
UserAdmin.fieldsets = tuple(fields)

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Member)