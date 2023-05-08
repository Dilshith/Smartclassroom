from django.shortcuts import render
from login.models import Login
# Create your views here.
from teacher.models import Teacher

# Create your views here.
def add_teacher(request):
    if request.method == 'POST':
        obj = Teacher()
        obj.username = request.POST.get('username')
        obj.department = request.POST.get('dept')
        obj.qualification = request.POST.get('qual')
        obj.address = request.POST.get('address')
        obj.email = request.POST.get('email')
        obj.phone = request.POST.get('phone')
        obj.status = 'pending'
        obj.save()

        ob=Login()
        ob.username=obj.username
        ob.password=obj.email
        ob.uid=obj.teacher_id
        ob.type='teacher'
        ob.save()
    return render(request,'teacher/teacher.html')

def view_teacher(request):
    obj = Teacher.objects.all()
    context = {
        'x': obj,
    }
    return render(request,'teacher/view teacher.html',context)
def approve(request,idd):
    obj=Teacher.objects.get(teacher_id=idd)
    obj.status = 'approve'
    obj.save()
    return view_teacher(request)
def reject(request,idd):
    obj=Teacher.objects.get(teacher_id=idd)
    obj.status = 'reject'
    obj.save()
    return view_teacher(request)




