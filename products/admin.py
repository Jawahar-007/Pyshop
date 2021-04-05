from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import product,offer

class productAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','image_url')

class offerAdmin(admin.ModelAdmin):
    list_display=('code','discount')

admin.site.register(product,productAdmin)
# Register your models here.
admin.site.register(offer,offerAdmin)


