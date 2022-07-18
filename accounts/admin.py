from django.contrib import admin
from accounts.models import Contact, Profile, Local

# Register your models here.
admin.site.register(Contact)
admin.site.register(Profile)
admin.site.register(Local)