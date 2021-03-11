from django.contrib import admin
from Accounts.models import User
from . import models

# Register your models here.


@admin.register(models.StaffMember)
class StaffMemberAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "related_teacher_account":
            kwargs["queryset"] = User.objects.filter(is_teacher=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(models.Wishlist)


admin.site.register(models.BestStudent)