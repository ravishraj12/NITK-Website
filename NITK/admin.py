from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(StudentData)
admin.site.register(Subjects)
admin.site.register(NewsUpdates)
admin.site.register(FacultyData)
admin.site.register(PlacementsUpdate)
admin.site.register(LoggedInUsers)