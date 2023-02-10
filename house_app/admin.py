from django.contrib import admin
from house_app.models import House


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    pass
