from datetime import date, datetime
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from agenda.models import AgendaClient, Event
from .models import Lid
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import LidForm
from .utils import paginateLeden, presentLid, searchLeden
from finance.models import Decla, Stand

# Create your views here.


def loginUser(request):
    # print(User.objects.all())
    # page = "login"
    if request.user.is_authenticated:
        return redirect("agenda")
    if request.method == "POST":
        username = request.POST["username"]  # .lower()
        password = request.POST["password"]
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.info(request, "User was logged in")
            return redirect(request.GET["next"] if "next" in request.GET else "agenda")
        else:
            messages.error(request, "Password is incorrect")

    return render(request, "users/login.html")


def logoutUser(request):
    logout(request)
    messages.info(request, "User logged out")
    return redirect("login")


@login_required(login_url="login")
def leden(request):
    #
    # lidlist, search_query = searchLeden(request)
    # custom_range, lidlist = paginateLeden(request, lidlist, 3)
    search_query = 0
    custom_range = 0
    ledenlist = Lid.objects.filter(active = True)
    content = {
        "leden": ledenlist,
        "search_query": search_query,
        "custom_range": custom_range,
        "stand": Stand.objects.get(owner_id=request.user.lid.id).amount,
    }
    return redirect("agenda")
    return render(request, "users/leden.html", content)


@login_required(login_url="login")
def userLid(request, pk):
    lid = Lid.objects.get(id=pk)
    content = {
        "lid": lid,
        "stand": Stand.objects.get(owner_id=lid.id).amount,
    }
    return render(request, "users/user-profile.html", content)


@login_required(login_url="login")
def userAccount(request):
    lid = request.user.lid
    content = {
        "lid": lid,
        "stand": Stand.objects.get(owner_id=lid.id).amount,
        "declasFILED": Decla.objects.filter(owner_id=lid.id),
        "declasPRESENT": presentLid(lid),
    }
    return render(request, "users/account.html", content)


@login_required(login_url="login")
def editAccount(request):
    lid = request.user.lid
    form = LidForm(instance=lid)
    content = {"form": form}
    if request.method == "POST":
        form = LidForm(request.POST, request.FILES, instance=lid)
        if form.is_valid():
            form.save()
            return redirect("account")
    content["stand"] = Stand.objects.get(owner_id=request.user.lid.id).amount
    return render(request, "users/leden-form.html", content)


def home(request):
    return render(request, "home.html")


def fakePage(request):
    return render(request, "main-page.html")


# def showCV(request, pk):
#     lid = Lid.objects.get(id=pk)
#     content = {'CV': None, 'lid': lid}
#     return render(request, 'users/document.html', content)


# def loadDATA(request):
#     # print(User.objects.all())
#     # return render(request, "home.html")
#     import pandas as pd

#     data = pd.read_excel("environment/das info.xlsx", sheet_name="Leden")
#     for user in data.iterrows():
#         user = user[1]
#         AC = AgendaClient.objects.get(name="nextID")
#         lichting = AgendaClient.objects.get(name="lichting")
#         vertical = AgendaClient.objects.get(name="vertical")
#         initials = AgendaClient.objects.get(name="initials")
#         name = AgendaClient.objects.get(name="name")
#         initials.json = user.initials
#         name.json = user.name
#         if user["jaar"] >= 90:
#             AC.json = 19 * 1000 + user["jaar"] * 10 + user["vertical"]
#             vertical.json = user.vertical
#             lichting.json = 19 * 100 + user["jaar"]
#         else:
#             AC.json = 20 * 1000 + user["jaar"] * 10 + user["vertical"]
#             vertical.json = user.vertical
#             lichting.json = 20 * 100 + user["jaar"]
#         AC.save()
#         lichting.save()
#         vertical.save()
#         initials.save()
#         name.save()
#         user = User.objects.create_user(username=user.username, password=user.password)
#     return render(request, "home.html")


def loadDATA(request):
    # print(User.objects.all())
    # return render(request, "home.html")
    import pandas as pd

    days = [
        "Maandag",
        "Dinsdag",
        "Woensdag",
        "Donderdag",
        "Vrijdag",
        "Zondag",
        "Maa",
        "Din",
        "Woe",
        "Don",
        "Vri",
        "Zat",
        "Zon",
        "Ma",
        "Di",
        "Wo",
        "Do",
        "Vr",
        "Za",
        "Zo",
    ]
    months = [
        "jan",
        "feb",
        "mrt",
        "apr",
        "mei",
        "juni",
        "juli",
        "aug",
        "sep",
        "okt",
        "nov",
        "dec",
    ]

    data = pd.read_excel("environment/das info.xlsx", sheet_name="Calendar")
    for event in data.iterrows():
        event = event[1]
        lis = str(event.Datum).split(" ")
        summary = event.Activiteit
        decription = event.Omschrijving

        if len(lis) == 3:
            let, day, month = lis
            try:
                day = int(day)
            except:
                continue
            if let in days:
                for index, m in enumerate(months):
                    if month.lower() == m:
                        month = index + 1
                        if month > 8:
                            year = 2021
                        else:
                            year = 2022
                        Event.objects.create(
                            summary=summary,
                            description=decription,
                            start_date=date(year, month, int(day)),
                            start_time=datetime.now(),
                            end_time=datetime.now(),
                        )
                        # print(summary, decription, datetime(year, month, day), datetime.now(), datetime.now())
                        break
        elif len(lis) == 4 and lis[1] == "t/m":
            start, tm, end, month = lis
            for index, m in enumerate(months):
                if month.lower() == m:
                    month = index + 1
                    if month > 8:
                        year = 2021
                    else:
                        year = 2022
                    # print(summary, decription, date(year, month, int(start)), datetime.now(), datetime.now())
                    Event.objects.create(
                        summary=summary,
                        description=decription,
                        start_date=date(year, month, int(start)),
                        start_time=datetime.now(),
                        end_time=datetime.now(),
                        end_date=date(year, month, int(end)),
                    )

                    break
        elif len(lis) == 6 and lis[1] in ["&", "t/m"]:
            let1, start, tm, let2, end, month = lis
            for index, m in enumerate(months):
                if month.lower() == m:
                    month = index + 1
                    if month > 8:
                        year = 2021
                    else:
                        year = 2022
                    # print(summary, decription, date(year, month, int(start)), datetime.now(), datetime.now())
                    Event.objects.create(
                        summary=summary,
                        description=decription,
                        start_date=date(year, month, int(start)),
                        start_time=datetime.now(),
                        end_time=datetime.now(),
                        end_date=date(year, month, int(end)),
                    )

                    break
        else:
            continue
        # print(event)

    return render(request, "home.html")
