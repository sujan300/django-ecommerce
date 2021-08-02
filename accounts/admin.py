from django.contrib import admin
from accounts.models import Account
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AdminAccount(UserAdmin):
    list_display        = ('id','email','username','first_name','last_name','last_login','date_joined','is_active','phone_number')
    list_display_links  = ('email','first_name','last_name','last_login',)
    readonly_fields     = ('last_login','date_joined')
    ordering            = ['-date_joined']
    filter_horizontal   = ()
    list_filter         = ()
    fieldsets           = ()
admin.site.register(Account,AdminAccount)



# @admin.register(Account,AdminAccount)
# class AdminAccount(admin.ModelAdmin):
#     list_display        = ('id','email','username','first_name','last_name','last_login','date_joined','is_active',)
#     filter_horizontal   = ()
#     list_filter         = ()
#     fieldsets           = ()