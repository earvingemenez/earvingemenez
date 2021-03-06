from django.contrib import admin
from .models import (
    Timeline,
    Project,
    Skill,
    Education,
    Interest,
    Feedback,
)


# Register to admin panel
admin.site.register(Timeline)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Interest)
admin.site.register(Feedback)