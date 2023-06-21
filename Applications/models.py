from django.db import models


# Create your models here.
class Application(models.Model):
    job_title = models.CharField(default="Software Developer", max_length=40)
    company_name = models.CharField(max_length=40)
    description_link = models.URLField()
    notes = models.TextField(null=True)
