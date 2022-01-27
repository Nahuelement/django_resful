from django.contrib import admin

from .models import Drone, Pilot, Competition



class PilotAdmin(admin.ModelAdmin):
    date_hierarchy = 'inserted_timestamp'
    #list_display = ('name', 'isbn')
    list_filter = ('gender','inserted_timestamp')
    search_fields = ('name', 'gender')

# Register your models here.
# admin_site = BookrAdminSite(name='bookr')



admin.site.register(Drone)
admin.site.register(Pilot,PilotAdmin)
admin.site.register(Competition)
