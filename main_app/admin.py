from django.contrib import admin

from .models import Pop, Detail, Accessory, Photo

# Register your models here
admin.site.register(Pop)

admin.site.register(Detail)

admin.site.register(Accessory)

admin.site.register(Photo)