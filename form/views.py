from django.shortcuts import render,HttpResponse
from .models import RegistrationForm

def index(request):
     # if request.method == 'POST' :
     #
     #     user_form = UserCreationForm(request.POST)
     #
     #     if user_form.is_valid() :
     #         user_form.save()
     #         return  render(request,'index.html')
     #     else :
     #            user_form = UserCreationForm()
     #            return render(request, 'registration.html', {'user_form' : user_form})
     # else:
     #    user_form = UserCreationForm()
     #    return render(request,'registration.html',{'user_form':user_form})
     return render(request, 'index.html')

def registration(request):
    if request.method=='POST':

        user_form=RegistrationForm(request.POST)

        if user_form.is_valid():
            user_form.save()
            return HttpResponse("<h1> Registration Successfully</h1>")
        else:
            return HttpResponse("<h1> Registration failed</h1>")

    else:
        user_form = RegistrationForm()
    return render(request,'registration.html',{'user_form':user_form})

