from django.contrib import admin
from home.models import Wish,Video,Gift

class wishAdmin(admin.ModelAdmin):
    list_display = ['name','message','relation']

class videoAdmin(admin.ModelAdmin):
    list_display = ['name','message','url']

class giftAdmin(admin.ModelAdmin):
    list_display = ['name','gift','email','gifttype','emailed']

# Register your models here.
admin.site.register(Wish,wishAdmin)
admin.site.register(Video,videoAdmin)
admin.site.register(Gift,giftAdmin)
