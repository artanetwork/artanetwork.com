from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Slide

# Register your models here.


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('title',)
