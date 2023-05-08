from django.shortcuts import render
from login.models import Login
from student.models import Student

# Create your views here.
def post_student(request):
    if request.method == 'POST':
        obj = Student()
        obj.roll_no = request.POST.get('rnbr')
        obj.age = request.POST.get('age')
        obj.gender = request.POST.get('gen')
        obj.username = request.POST.get('username')
        obj.password = request.POST.get('pass')
        obj.age = request.POST.get('age')
        obj.department = request.POST.get('dep')
        obj.email = request.POST.get('email')
        obj.phone = request.POST.get('phone')
        obj.status = 'pending'
        obj.save()

        ob = Login()
        ob.username = obj.username
        ob.password = obj.password
        ob.uid = obj.student_id
        ob.type = 'student'
        ob.save()
    return render(request,'student/student.html')

def view_student(request):
    obj = Student.objects.all()
    context = {
        'x': obj,
    }
    return render(request,'student/view_student.html',context)

def vsadmn(request):
    obj = Student.objects.all()
    context = {
        'x': obj,
    }
    return render(request,'student/vstdnr_admin.html',context)


def approve(request,idd):
    obj=Student.objects.get(student_id=idd)
    obj.status = 'approve'
    obj.save()
    return view_student(request)
def reject(request,idd):
    obj=Student.objects.get(student_id=idd)
    obj.status = 'reject'
    obj.save()
    return view_student(request)

