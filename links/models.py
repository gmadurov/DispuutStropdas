from django.db import models

# Create your models here.
class Links(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    link = models.URLField(max_length=200)
    def __str__(self):
        return str(self.name)