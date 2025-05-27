from django.contrib import admin
# Register your models here.
from .models import Profile, Book, SupportMessage  # Make sure these are imported

class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "role", "student_id"]
    search_fields = ["user__username", "student_id"]  # Use double underscores for related fields

class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "available"]
    list_filter = ["available"]
    search_fields = ["title", "author"]

class SupportMessageAdmin(admin.ModelAdmin):
    list_display = ["user", "subject", "created_at"]
    search_fields = ["user__username", "subject"]
    readonly_fields = ["created_at"]

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(SupportMessage, SupportMessageAdmin)



