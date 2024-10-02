from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

admin.site.register(ProductCategory)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Maker)
admin.site.register(Profile)


# mix Profile info and user info
class ProfileInline(admin.StackedInline):
    model = Profile


# Extend User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    field = ["username", "first_name", "last_name", "email"]
    inlines = [ProfileInline]


# unregister the old user model
admin.site.unregister(User)

# register the new user model
admin.site.register(User, UserAdmin)
