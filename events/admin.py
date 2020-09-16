from django.contrib import admin
from .models import Category, Organiser, Person, Program, Schedule, Speaker

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug':['name']}
    ordering = ['name']
    search_fields = ['name']

#
# @admin.register(Event)
# class EventAdmin(admin.ModelAdmin):
#     """
#     Customize Event Section Admin Panel
#     """
#     pass
#
# @admin.register(File)
# class FileAdmin(admin.ModelAdmin):
#     """
#     Customize File Section Admin Panel
#     """
#     pass

@admin.register(Organiser)
class OrganizerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'website', 'date_added')
    search_fields = ['name', 'email']
    ordering = ['name']
    list_filter = ('date_added', 'date_edited')


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'contact_number')
    search_fields = ['full_name']
    ordering = ['full_name']

@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'link')
    ordering = ['name']
    search_fields = ['name']

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    """
    Customize Schedule Section Admin Panel
    """
    pass

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title' , 'description', 'time', 'speaker')


    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    time = models.DateTimeField()
    speaker = models.ForeignKey(Speaker, models.DO_NOTHING)
