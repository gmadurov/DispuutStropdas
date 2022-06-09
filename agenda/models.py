from django.db import models

from users.models import Lid

# Create your models here.


class AgendaClient(models.Model):
    # lid = models.OneToOneField(Lid, on_delete=models.CASCADE)
    # token = models.CharField(max_length=200, null=True, blank=True)
    # refresh_token = models.CharField(max_length=200, null=True, blank=True)
    # token_uri = models.CharField(max_length=200, null=True, blank=True)
    # client_id = models.CharField(max_length=200, null=True, blank=True)
    # client_secret = models.CharField(max_length=200, null=True, blank=True)
    # scopes = models.CharField(max_length=2000, null=True, blank=True)
    # expiry = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=30, null=True, blank=True, unique=True)
    json = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Event(models.Model):
    EVENT_CHOICES = (
        ("Activiteit", "Activiteit"),
        ("Borrel", "Borrel"),
        ("Clubactiviteit", "Clubactiviteit"),
        ("Wedstrijd", "Wedstrijd"),
        ("Dispuutsactiviteit", "Dispuutsactiviteit"),
        ("Dispuutsverjaardag", "Dispuutsverjaardag"),
        ("Dispuutsavonds", "Dispuutsavonds"),
        ("AdministratifActivitied", "AdministratifActivitied"),
        ("Bier", "Bier"),
    )
    BIJZONDERHEIDEN = (
        ("Op Afmelding", "Op Afmelding"),
        ("Op Aanmelding", "Op Aanmelding"),
        (" ", " "),
    )
    # summary,description,start_date,start_time,end_date,end_time,recuring,location,koker,kartrekkers,info,budget, bijzonderheden
    summary = models.CharField(max_length=50, choices=EVENT_CHOICES)
    description = models.CharField(max_length=50, null=True, blank=True)
    start_date = models.DateField()
    start_time = models.TimeField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    recuring = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    kokers = models.ManyToManyField(Lid, blank=True, related_name="kookshift")
    kartrekkers = models.CharField(max_length=50, null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    budget = models.CharField(max_length=50, null=True, blank=True)
    bijzonderheden = models.CharField(
        max_length=50, default="Op Afmelding", choices=BIJZONDERHEIDEN
    )
    google_link = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return str(self.description) + ", " + str(self.start_date)

    class Meta:
        ordering = ["start_date", "start_time", "-end_date"]


class NIEvent(models.Model):
    """DSANI events links"""

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="dsani_ev")
    lid = models.ForeignKey(Lid, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    note = models.CharField(default="", max_length=200, null=True, blank=True)

    def __str__(self):
        if self.note:
            return str(self.lid.initials) + ", " + str(self.note)
        return str(self.lid.initials) + ", " + str(self.event.description)

    class Meta:
        ordering = ["event"]
