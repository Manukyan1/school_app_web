from django.contrib import admin
from .models import *
admin.site.register(puple)
admin.site.register(gender)

admin.site.site_title = 'Classroom'
admin.site.site_header = 'Classroom Administration'
