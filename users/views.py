from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import  Lid
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import LidForm
from .utils import paginateLeden, searchLeden
# Create your views here.


def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('leden')
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.info(request, 'User was logged in')
            return redirect(request.GET['next']if 'next' in request.GET else 'account')
        else:
            messages.error(request, 'Password is incorrect')

    return render(request, 'users/login-register.html')


def logoutUser(request):
    logout(request)
    messages.info(request, "User logged out")
    return redirect('login')


@login_required(login_url='login')
def leden(request):
    lidlist, search_query = searchLeden(request)
    custom_range, lidlist = paginateLeden(request, lidlist, 3)
    content = {'leden': lidlist,
               'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'users/leden.html', content)


@login_required(login_url='login')
def userLid(request, pk):
    lid = Lid.objects.get(id=pk)
    content = {'lid': lid}
    return render(request, 'users/user-profile.html', content)


@login_required(login_url='login')
def userAccount(request):
    lid = request.user.lid
    content = {'lid': lid,}
    return render(request, 'users/account.html', content)


@login_required(login_url='login')
def editAccount(request):
    lid = request.user.lid
    form = LidForm(instance=lid)
    content = {'form': form}
    if request.method == 'POST':
        form = LidForm(request.POST, request.FILES, instance=lid)
        if form.is_valid():
            form.save()
            return redirect('account')

    return render(request, 'users/leden-form.html', content)

def home(request):
    return render(request, 'home.html')
def fakePage(request):
    return render(request, 'main-page.html')

# def showCV(request, pk):
#     lid = Lid.objects.get(id=pk)
#     content = {'CV': None, 'lid': lid}
#     return render(request, 'users/document.html', content)
