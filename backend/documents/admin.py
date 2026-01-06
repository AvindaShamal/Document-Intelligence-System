from django.contrib import admin
from .models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("id", "owner", "title", "status", "uploaded_at")
    search_fields = (
        "title",
        "id",
    )
    list_filter = ("status",)
