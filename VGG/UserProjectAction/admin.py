from django.contrib import admin
from .models import UserProfile,Project,Action
admin.site.register(UserProfile)
# Register your models here.
admin.site.register(Project)
admin.site.register(Action)


