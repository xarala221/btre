from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from contacts.models import Contact

def register(request):
  
  if request.method == "POST":
    #Get form values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    #check if password much
    if password == password2:
      pass
      #check username
      if User.objects.filter(username=username).exists():
        messages.error(request, "That username is taken")
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, "That email is being used")
          return redirect('register')
        else :
          #looks good
          user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
          # auth.login(request, user)
          # messages.success(request, "You are logged in")
          # return redirect(request, "index")
          user.save()
          messages.success(request, "You are now registred and can log  in")
          return redirect("login")
    else:
      messages.error(request, "Password didn't match")
      return redirect('register')
    #Resgister user
    print("e")
  else:
    context = {}
    return render(request, "accounts/register.html", context)

def login(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
      auth.login(request, user)
      messages.success(request, "You now log in")
      return redirect("dashboard")
    else:
      messages.error(request, "Invalid creadentiel")
      return redirect("login")

  else:
    #context = {}
    return render(request, "accounts/login.html")

def logout(request):
  if request.method == "POST":
    auth.logout(request)
    messages.success(request, "You are log out")
    return redirect('index')

def dashboard(request):
  user_contacts = Contact.objects.order_by('contact_date').filter(user_id=request.user.id)
  context = {
    "contacts":user_contacts
  }
  return render(request, "accounts/dashboard.html", context)
