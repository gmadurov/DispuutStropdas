from multiprocessing import context
from django.shortcuts import redirect, render

from documents.forms import DocumentForm
from finance.models import Stand
import numpy as np

from .models import Document
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import DocumentForm
from django.db.models import Q


def roman(num):
    res = ""
    table = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]
    for cap, roman in table:
        d, m = divmod(num, cap)
        res += roman * d
        num = m

    return res


# Create your views here.
@login_required(login_url="login")
def addDocument(request):
    form = DocumentForm()
    content = {
        "form": form,
        "stand": Stand.objects.get(owner_id=request.user.lid.id).amount,
    }
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        condi = len(request.FILES) == 0
        for k, v in request.FILES.items():
            if k == "file" and (v.name.endswith(".pdf") or v == None):
                condi = True
                break
            else:
                condi = False
        if form.is_valid():
            if condi:
                document = form.save(commit=False)
                document.owner = request.user.lid
                document.save()
                return redirect("documents")
            else:
                messages.error(request, "Document upload has to be a a pdf")
        else:
            messages.error(request, "an error occurred while creating document")
            return redirect("documents")
            # return redirect("documents")
    return render(request, "documents/document-form.html", content)


@login_required(login_url="login")
def editDocument(request, pk):
    document = Document.objects.get(id=pk)
    form = DocumentForm(instance=document)
    content = {
        "form": form,
        "stand": Stand.objects.get(owner_id=request.user.lid.id).amount,
    }
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES, instance=document)
        condi = len(request.FILES) == 0
        # condi = True
        for k, v in request.FILES.items():
            if k == "file" and (v.name.endswith(".pdf") or v == None):
                condi = True
                break
            else:
                condi = False
        if form.is_valid():
            if condi:
                document = form.save(commit=False)
                document.owner = request.user.lid
                document.save()
                return redirect("documents")
            else:
                messages.error(request, "CV upload has to be a a pdf")
        else:
            messages.error(request, "an error occurred while updating document")
            return redirect("documents")
    return render(request, "documents/document-form.html", content)


@login_required(login_url="login")
def deleteDocument(request, pk):
    document = Document.objects.get(id=pk)
    if request.method == "POST":
        document.delete()
        messages.info(request, "Document deleted")
        return redirect("Documents")
    content = {
        "object": document,
        "stand": Stand.objects.get(owner_id=request.user.lid.id).amount,
    }
    return render(request, "delete-template.html", content)


@login_required(login_url="login")
def showDocument(request, pk):
    document = Document.objects.get(id=pk)
    content = {
        "document": document,
        "stand": Stand.objects.get(owner_id=request.user.lid.id).amount,
    }
    return render(request, "documents/document.html", content)


@login_required(login_url="login")
def showDocumentsPerYear(request, year):
    documents = Document.objects.filter(senate_year__exact=year)
    years = [
        (roman(i), i)
        for i in np.unique(
            np.array([doc.senate_year for doc in Document.objects.all()])
        )
    ]
    content = {
        "documents": documents,
        "years": years,
        "stand": Stand.objects.get(owner_id=request.user.lid.id).amount,
    }
    return render(request, "documents/documents.html", content)


@login_required(login_url="login")
def showDocuments(request):
    documents = Document.objects.all()
    years = [
        (roman(i), i)
        for i in np.unique(np.array([doc.senate_year for doc in documents]))
    ]
    content = {
        "documents": documents,
        "years": years,
        "stand": Stand.objects.get(owner_id=request.user.lid.id).amount,
    }
    return render(request, "documents/documents.html", content)
