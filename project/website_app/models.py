from django.db import models

class JobProfile(models.Model):
    jobTitle = models.CharField(max_length=100)
    jobLocation = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    jobDescription = models.CharField(max_length=500, null=True)
    validThroughDate = models.DateField()
