from django.contrib import admin

# Register your models here.
from django.contrib.admin.decorators import register
from .models import *


class ActionTagAdmin(admin.ModelAdmin):
    filter_horizontal = ("tag_job",)


class ActionAdmin(admin.ModelAdmin):
    list_display = ("position", "action", )


# Register your models here.
admin.site.register(Company)
admin.site.register(Position)
admin.site.register(Action, ActionAdmin)
admin.site.register(TagJob)
admin.site.register(Skill, ActionTagAdmin)
admin.site.register(Education, ActionTagAdmin)

