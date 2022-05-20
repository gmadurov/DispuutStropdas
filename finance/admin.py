from django.contrib import admin

from finance.models import Bier, Boekstuk, Decla,Stand

# Register your models here.
admin.site.register(Decla)
admin.site.register(Stand)
admin.site.register(Boekstuk)
admin.site.register(Bier)
