from django.contrib import admin


class TimeStampedModelAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")


class ArchivableModelAdmin(admin.ModelAdmin):
    readonly_fields = ("is_archived",)
