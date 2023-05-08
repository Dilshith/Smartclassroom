from django.shortcuts import render
from teacher.models import Teacher
from student.models import Student
from chat.models import Chat
from django.db.models import Q
import datetime
# Create your views here.
from login.models import Login


def user(request):
    ob= Teacher.objects.all()
    context={
        'u':ob
    }
    return render(request,'chat/view user.html',context)




def adchat(request,idd):
    ss=request.session["uid"]
    obj = Teacher.objects.get(teacher_id=idd)
    ob = Chat.objects.filter(Q(student_id=ss) & Q(teacher_id=idd))
    context = {
        'kk': ob,
        'uu': obj,
    }

    if request.method == 'POST':
        obk = Chat()
        obk.message = request.POST.get('mssg')
        obk.teacher_id=idd
        obk.student_id=ss
        obk.rectype="teacher"
        obk.sendtype="student"
        obk.save()
    return render(request, 'chat/chatuser1.html',context)


def student(request):
    ob= Student.objects.all()
    context={
        'u':ob
    }
    return render(request,'chat/view student.html',context)

# emaildef student(request):
#     # ss=request.session['uid']
#     # stid=Chat.objects.filter(teacher_id=ss,status='pending')
#     # st=[]
#     # for s in stid:
#     #     st.append(s.student_id)
#     #
#     #
#     # print(stid)
#     # ob= Student.objects.filter(student_id__in=st)
#     ob = Chat.objects.all()
#     context={
#         'u':ob
#     }
#     return render(request,'chat/view student.html',context)
#



def cust(request,idd):
    ss = request.session["uid"]
    obj = Student.objects.get(student_id=idd)
    ob=Chat.objects.filter(Q(student_id=idd) & Q(teacher_id=ss))
    context={
        'kk':ob,
        'uu':obj,
    }
    if request.method=='POST':
        obk = Chat()
        obk.message = request.POST.get('mssg')
        obk.teacher_id=ss
        obk.student_id=idd
        obk.rectype="student"
        obk.sendtype="teacher"
        obk.save()
    return render(request, 'chat/chatuser2.html',context)
