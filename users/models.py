from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Lid(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    initials = models.CharField(max_length=4, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    educations = models.CharField(max_length=200, null=True, blank=True)
    lichting = models.IntegerField()
    vertical = models.IntegerField()
    email = models.EmailField(max_length=500, blank=True)
    phone = models.CharField(max_length=500, null=True, blank=True, unique=True)
    short_intro = models.CharField(max_length=200, null=True, blank=True)
    lid_image = models.ImageField(
        upload_to="images/leden/",
        null=True,
        blank=True,
        default="images/leden/user-default.png",
    )

    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.IntegerField(default=0, primary_key=True, unique=True)

    def __str__(self):
        return str(self.user.username)

    @property
    def imageURL(self):
        try:
            url = self.lid_image.url
        except:
            url = ""
        return url

    class Meta:
        ordering = ["lichting", "vertical"]
