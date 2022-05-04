from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import DeclaForm
from .models import Decla, Stand

# Create your views here.


def fileDecla(request):
    form = DeclaForm()
    if request.method == "POST":
        form = DeclaForm(request.POST, request.FILES)
        if form.is_valid():
            decla = form.save(commit=False)
            decla.owner = request.user.lid
            decla.save()
            messages.info(request, "Decla was created")
            return redirect("agenda")
    context = {
        "form": form,
        "stand": Stand.objects.get(owner_id=request.user.lid.id).amount,
    }
    return render(request, "finance/decla_form.html", context)


def editDecla(request, pk):
    decla = Decla.objects.get(id = pk)
    form = DeclaForm(instance= decla)
    if request.method == "POST":
        form = DeclaForm(request.POST, request.FILES,instance= decla)
        if form.is_valid():
            print('SSSSUUUBBBMMMIIITTTTEEEDDD')
            decla = form.save(commit=False)
            # "taken out because the owner is the one who 
            # creates it to avoid problems when edditing from sennate"
            # decla.owner = request.user.lid
            decla.save()
            messages.info(request, "Decla was created")
            return redirect("agenda")
        else:
            print('save failed####################')
    context = {
        "form": form,
        "stand": Stand.objects.get(owner_id=request.user.lid.id).amount,
    }
    return render(request, "finance/decla_form.html", context)


def deleteDecla(request, pk):
    decla = Decla.objects.get(id=pk)
    if request.method == "POST":
        decla.delete()
        messages.info(request, 'Decla deleted')
        return redirect('account')
    content = {'object': decla}
    return render(request, 'delete-template.html', content)


def showDecla(request, pk):
    decla = Decla.objects.get(id = pk)
    form = DeclaForm(instance= decla) 
    content = {'form': form}
    return render(request, 'finance/show_decla.html', content)

