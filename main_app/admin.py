from django.contrib import admin
from django.contrib.auth.models import User

from main_app.models import Profile, Pet, PetPhoto


class PetInLineAdmin(admin.StackedInline):
    model = Pet

# TODO: inline to user in admin site
# class UserCustom(User):
#     pass
#
# @admin.register(UserCustom)
# class UserAdmin(admin.ModelAdmin):
#     inlines = (PetInLineAdmin, )



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # inlines = (PetInLineAdmin, )
    pass


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass


@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    pass
