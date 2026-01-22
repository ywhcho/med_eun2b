from django.contrib import admin
from .models import Medicine

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ['drug_name', 'company', 'ingredient', 'created_at']
    list_filter = ['company', 'created_at']
    search_fields = ['drug_name', 'ingredient', 'company', 'efficacy']
    readonly_fields = ['created_at']

