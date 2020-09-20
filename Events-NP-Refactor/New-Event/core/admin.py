from django.contrib import admin
from .models import Contact, FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    """
    Customize FAQ section Admin panel
    """
    pass

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Customize Contact section Admin panel
    """
    pass