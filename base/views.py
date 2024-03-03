from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import MyUserCreationForm , DetailsForm
from django.contrib.auth import login , authenticate , logout
from .models import User , Details
from django.db.models import Q


# Create your views here.
def home(request):
   q = request.GET.get('q') if request.GET.get('q') != None else '' #if theres nothing in q set the value of q to ''
   #  details = Details.objects.filter(details__number__contains=q) this only gives a searhc funtionality that searches using the topic name
   # details = Details.objects.filter(
   #    Q(phone_number__phone_number__contains=q) 
   # )

   context = {'details':details}
   return render(request , 'base/home.html', context)

def signup(request):
    page = 'signup'

    if request.user.is_authenticated:
      return redirect('home')

    form = MyUserCreationForm()
    
    if request.method == 'POST':
      form = MyUserCreationForm(request.POST)
      if form.is_valid():
         user = form.save(commit=False)
         user.username = user.username.lower()
         user.save()

         group = Group.objects.get(name='Students')
         user.groups.add(group)
         username = form.cleaned_data.get('username')
         messages.success(request, f'Account successfully created for {username}')

         login(request, user)
         return redirect('home')
      # else:
      #    messages.error(request , 'An error has occured during registration')


    context = {'page':page, 'form':form}
    return render(request , 'base/login_register.html', context)

def loginPage(request):
   page = 'login'

   if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')

      try:
         user = User.objects.get(username=username)
         
      except:
         messages.error(request, 'User does not exist')
      
      user = authenticate(request, username=username , password=password)
      if user is not None:
         login(request, user)
         return redirect('home')
      else:
         messages.error(request, 'Username or Password doesnt exist')


   context = {'page':page}
   return render(request, 'base/login_register.html', context)


def logoutPage(request):
    logout(request)
    return redirect('home')

def addDetails(request):
    form = DetailsForm()
    if request.method == 'POST':
      form = DetailsForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('home')
    context = {'form':form}
    return render(request, 'base/details.html')
