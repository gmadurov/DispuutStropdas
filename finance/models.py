import uuid
from datetime import datetime
from multiprocessing import Event

import pandas as pd
from requests import request
from agenda.models import Event
from django.db import models
from django.http import HttpResponse, FileResponse
from documents.models import Document
from users.models import Lid


# Create your models here.
def senate_jaar():
    date = datetime.today()
    month = int(date.strftime("%m"))
    year = int(date.strftime("%Y")) - 1990
    if month >= 9:
        out = year + 1
    else:
        out = year
    return out


class Boekstuk(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ["name"]


class Decla(models.Model):
    # owner, event, content, total, present, senate_year, receipt, reunist, kmters, verwerkt
    owner = models.ForeignKey(Lid, default=19900, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField(max_length=50)
    total = models.FloatField()
    present = models.ManyToManyField(Lid, related_name="present_leden")
    receipt = models.ImageField(
        upload_to="declas/", null=True, blank=True
    )  ## this will need to be put back to nothing when it ends
    reunist = models.IntegerField(default=0)
    kmters = models.IntegerField(default=0)

    boekstuk = models.ForeignKey(
        Boekstuk, on_delete=models.SET_NULL, null=True, blank=True
    )
    content_ficus = models.TextField(max_length=100, null=True, blank=True)
    senate_year = models.IntegerField(default=senate_jaar())
    verwerkt = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return str(self.event) + " " + str(self.owner)

    @property
    def imageURL(self):
        try:
            url = self.receipt.url
        except:
            url = ""
        return url

    class Meta:
        ordering = ["event"]

    def export():
        # response = FileResponse(content_type="application/vnd.ms-excel",file_to_stream=df)
        # response["Content-Disposition"] = 'attachment; filename="declas.xlsx"'

        MT = (
            ["Mutatie", "Totaal"]
            for lid in range(len(Lid.objects.filter(active=True)) + 3)
        )
        rows = [
            [
                "Datum",
                "Boekstuk",
                "Omshrijven",
            ]
            + [item for sublist in MT for item in sublist]
        ]
        leden = Lid.objects.all()
        rows.append(
            ["", "", "Start Stand"]
            + [
                item
                for sublist in (
                    [0, stand.initial_amount] for stand in Stand.objects.all()
                )
                for item in sublist
            ]
        )

        for index, decla in enumerate(Decla.objects.filter(verwerkt=True)):
            cont = True
            row = [
                decla.event.start_date,
                decla.boekstuk,
                decla.content_ficus,
            ]
            present_leden = decla.present.all()
            try:
                amount_pp = round(
                    decla.total
                    / (len(present_leden) + int(decla.reunist) + int(decla.kmters)),
                    3,
                )
            except:
                amount_pp = round(decla.total, 3)
            if decla.owner.id == 19900:
                for i in range(4):
                    row.append(0)
                row.append(round(-decla.total, 2))
                for i in range((len(leden) * 2) + 1):
                    row.append(0)
                cont = False
            if cont:
                for i in range(0, 6):
                    row.append(0)
                for lid in leden:
                    for i in range(2):
                        # the range of 2 adds columns for mutatie and totaal for the sheet
                        # declared money is added to stand immidiatly and taken away if lid is present
                        if lid in present_leden and i == 0 and lid != decla.owner:
                            row.append(round(-amount_pp, 3))
                        elif lid in present_leden and i == 0 and decla.owner == lid:
                            row.append(round(decla.total - amount_pp, 2))
                        else:
                            row.append(0)

            for i in range(4, len(row), 2):
                try:
                    row[i] = round(rows[-1][i] + row[i - 1], 3)
                except:
                    row[i] = round(row[i - 1], 3)
            rows.append(row)
        df = pd.DataFrame(
            rows,
            columns=[
                "Dispuut Stropdas",
                " ",
                " ",
                # "Kast",
                # " ",
                # "Bank",
                # " ",
                # "Dispuut",
                # " ",
            ]
            + [lid.initials for lid in Lid.objects.all() for i in range(2)],
        )
        # # resp = HttpResponse(content_type="text/csv")
        # # resp["Content-Disposition"] = "attachment; filename=myFile.csv"
        # response = HttpResponse(
        #     df,
        #     content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        # )
        # response["Content-Disposition"] = 'attachment; filename="declas.xlsx"'
        # df.to_excel( "finance/Test_excel.xlsx")
        # Document.objects.get_or_create(name ='exportdeclas.xlsx', file = df.to_excel("Test_excel.xlsx"))
        # print(df)
        return 0, df.to_html()


class Stand(models.Model):
    owner = models.ForeignKey(Lid, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    initial_amount = models.FloatField(default=0)

    def __str__(self):
        return str(self.owner) + ", €" + str(self.amount)


class Bier(models.Model):
    inkoop_number = models.IntegerField(default=0)
    inkoop_cost = models.FloatField(default=0)
    uitkoop_number = models.IntegerField(default=0)

    @property
    def cost(self):
        return self.inkoop_cost / self.inkoop_number
