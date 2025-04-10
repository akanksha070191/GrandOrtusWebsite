from django.contrib import admin
from .models import JobProfile

class JobAdmin(admin.ModelAdmin):
    list_display = ['id', 'jobTitle', 'jobLocation', 'jobDescription', 'jobLocation', 'designation', 'validThroughDate']

admin.site.register(JobProfile, JobAdmin)
