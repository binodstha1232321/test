from django.contrib import admin
from .models import Category, Organiser, Person, Program, Schedule, Speaker

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Customize Category Section Admin Panel
    """
    pass
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
    """
    Customize Organizer Section Admin Panel
    """
    pass

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    """
    Customize Person Section Admin Panel
    """
    pass

@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    """
    Customize Speaker Section Admin Panel
    """
    pass

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    """
    Customize Schedule Section Admin Panel
    """
    pass

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    """
    Customize Program Section Admin Panel
    """
    pass
