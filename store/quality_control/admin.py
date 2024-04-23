from django.contrib import admin
from .models import BugReport
from .models import FeatureRequest

# Register your models here.
class BugReportAdminInline(admin.TabularInline):
    model = BugReport
    extra = 0
    list_display = ('title','project', 'status', 'priority', 'created_at')
    list_filter = ('title', 'status')
    search_fields = ('title', 'status')
    ordering = ('created_at',)
    list_editable = ('status',)
    readonly_fields = ('created_at',)
    can_delete = True
    show_change_link = True

@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title','project', 'status', 'priority', 'created_at')
    list_filter = ('title', 'status')
    search_fields = ('title', 'status')
    ordering = ('created_at',)
    list_editable = ('status',)
    readonly_fields = ('created_at',)


@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority', 'created_at')
    list_filter = ('title', 'status')
    search_fields = ('title', 'status')
    ordering = ('created_at',)
    list_editable = ('status',)
    readonly_fields = ('created_at',)
