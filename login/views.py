from django.shortcuts import render
from login.models import Login
from django.http import HttpResponseRedirect
from django.contrib import messages


# Create your views here.
def post_login(request):
    if request.method=="POST":
        name = request.POST.get('name')
        password = request.POST.get("psw")
        obj = Login.objects.filter(username=name , password=password)
        tp = ""
        for ob in obj:
           tp = ob.type
           uid = ob.uid
           if tp == "admin":
              request.session["uid"] = uid
              return HttpResponseRedirect('/temp/admin/')
           elif tp == "teacher":
               request.session["uid"] = uid
               return HttpResponseRedirect('/temp/teacher/')
           elif tp == "student":
               request.session["uid"] = uid
               return HttpResponseRedirect('/temp/student/')
        else:
           messages.info(request, 'Password or Username is incorrect')
           # message = "incorrect username or password....please try again....!"
           # context ={
           #     'message': message,
           # }
           return render (request,'login/login.html')#,context)
    return render(request,'login/login.html')



