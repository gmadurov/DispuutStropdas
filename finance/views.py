from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import DeclaForm, FicusForm
from .models import Decla, Stand

# Create your views here.


@login_required(login_url="login")
def fileDecla(request):
    form = DeclaForm()
    if request.method == "POST":
        print(1, request.POST)
        form = DeclaForm(request.POST, request.FILES)
        if form.is_valid():
            print(form)
            decla = form.save()
            # decla = form.save(commit=False)
            decla.owner = request.user.lid
            # decla.present.set(request.POST["present"])
            print(2, decla.present.all())
            print(3, decla)
            decla.save()
            messages.info(request, "Decla was created")
            return redirect("agenda")
    context = {
        "form": form,
        "stand": Stand.objects.get(owner_id=request.user.lid.id).amount,
    }
    return render(request, "finance/decla_form.html", context)


@login_required(login_url="login")
def editDecla(request, pk):
    decla = Decla.objects.get(id=pk)
    form = DeclaForm(instance=decla)
    if request.method == "POST":
        print(request.POST)

        form = DeclaForm(request.POST, request.FILES, instance=decla)
        if form.is_valid():
            # print(form)
            # decla = form.save(commit=False)
            decla = form.save()
            # "taken out because the owner is the one who
            # creates it to avoid problems when edditing from sennate"
            # decla.owner = request.user.lid
            # decla.save()
            messages.info(request, "Decla was edited")
            return redirect(request.GET["next"] if "next" in request.GET else "agenda")
    context = {
        "form": form,
        "stand": Stand.objects.get(owner_id=request.user.lid.id).amount,
    }
    return render(request, "finance/decla_form.html", context)


@login_required(login_url="login")
def deleteDecla(request, pk):
    decla = Decla.objects.get(id=pk)
    if request.method == "POST":
        decla.delete()
        messages.info(request, "Decla deleted")
        return redirect(request.GET["next"] if "next" in request.GET else "agenda")
    content = {
        "object": decla,
        "stand": Stand.objects.get(owner_id=request.user.lid.id).amount,
    }
    return render(request, "delete-template.html", content)


@login_required(login_url="login")
def showDecla(request, pk):
    decla = Decla.objects.get(id=pk)
    content = {
        "decla": decla,
        "stand": Stand.objects.get(owner_id=request.user.lid.id).amount,
    }
    return render(request, "finance/show_decla.html", content)


@login_required(login_url="login")
def verwerkenDecla(request):
    declas = Decla.objects.all()
    # form = DeclaForm(instance= decla)
    content = {
        "declas": declas,
        "stand": Stand.objects.get(owner_id=request.user.lid.id).amount,
    }
    return render(request, "finance/verwerken_decla.html", content)


def exportDeclas(request):
    declas = Decla.export()
    content = {"object": declas[1]}

    # return declas[0]
    return render(request, "display.html", content)
