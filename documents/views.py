from multiprocessing import context
from django.shortcuts import redirect, render

from documents.forms import DocumentForm

from .models import Document
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import DocumentForm
from django.db.models import Q

# Create your views here.
def addDocument(request):
    form = DocumentForm()
    content = {'form': form}
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        condi = (len(request.FILES) == 0)
        for k, v in request.FILES.items():
            if k == 'file' and (v.name.endswith('.pdf') or v == None):
                condi = True
                break
            else:
                condi = False
        if condi:
            if form.is_valid():
                document = form.save(commit = False)
                document.owner = request.user.lid
                document.save()
                return redirect('documents')
            else:
                messages.error(
                    request, 'an error occurred while creating document')
                return redirect('documents')
        else:
            messages.error(request, 'CV upload has to be a a pdf')
            return redirect('documents')
    return render(request, 'documents/document-form.html', content)


def editDocument(request, pk):
    document = Document.objects.get(id=pk)
    form = DocumentForm(instance=document)
    content = {'form': form}
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, instance=document)
        condi = (len(request.FILES) == 0)
        for k, v in request.FILES.items():
            if k == 'file' and (v.name.endswith('.pdf') or v == None):
                condi = True
                break
            else:
                condi = False
        if condi:
            if form.is_valid():
                document = form.save(commit = False)
                document.owner = request.user.lid
                document.save()
                return redirect('documents')
            else:
                messages.error(
                    request, 'an error occurred while updating document')
                return redirect('documents')
        else:
            messages.error(request, 'CV upload has to be a a pdf')
            return redirect('documents')
    return render(request, 'documents/document-form.html', content)


def deleteDocument(request, pk):
    document = Document.objects.get(id=pk)
    if request.method == "POST":
        document.delete()
        messages.info(request, 'Document deleted')
        return redirect('Documents')
    content = {'object': document}
    return render(request, 'delete-template.html', content)


def showDocument(request, pk): 
    document = Document.objects.get(id= pk)
    content = {'document': document}
    return render(request,'documents/document.html', content)

def showDocumentsPerYear(request, year):
    documents = Document.objects.filter(senate_year__exact=year)
    years = [ doc.senate_year for doc in Document.objects.all()]
    content = {'documents': documents, 'years': years}
    return render(request,'documents/documents.html', content)

def showDocuments(request):
    documents = Document.objects.all()
    years = [ doc.senate_year for doc in documents]
    content = {'documents': documents, 'years': years}
    return render(request,'documents/documents.html', content)