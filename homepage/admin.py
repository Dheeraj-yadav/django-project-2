from django.contrib import admin
from .models import product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(product, ProductAdmin)
