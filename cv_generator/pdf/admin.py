from django.contrib import admin

from cv_generator.pdf.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
