from django.contrib import admin

# Register your models here.
import models

class pairAdmin(admin.ModelAdmin):
    list_display = ('id','question','answer','rate')
admin.site.register(models.Pair,pairAdmin)
admin.site.register(models.User)