from django.contrib import admin

# Register your models here.
from .models import TextContent,Home_card

admin.site.register(TextContent)
admin.site.register(Home_card)