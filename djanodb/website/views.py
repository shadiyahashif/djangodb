import email
from django.shortcuts import render,redirect
from .models import Member
from .forms import MemberForm
from django.contrib import messages
# Create your views here.

def home(request):
    all_members=Member.objects.all
    mydic= {
        "all" : all_members
     } 
    return render(request , "home.html" ,context=mydic)

def join(request):
    if request.method == "POST":
        form=MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
               
            fname = request.POST['f_name']
            lname = request.POST['l_name']
            age = request.POST['age']
            email = request.POST['email']
            password = request.POST['password']

            messages.success(request, ('There was an error in your Form ! Please try again ...')) 
            #return redirect('join')
            mydictionary= {
              'f_name':fname,'l_name':lname, 'age' : age ,
              'email':email , 'password':password
              }
              
            return render(request , "join.html",context=mydictionary)
   
            


        messages.success(request,('Your Form Has been Submitted Successfully'))   
        return render(request,"joinsuccess.html")    

    else:
        return render(request , "join.html")
   
