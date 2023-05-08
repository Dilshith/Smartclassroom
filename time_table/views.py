from django.shortcuts import render
from department.models import Department
from time_table.models import TimeTable
from django.core.files.storage import FileSystemStorage
# Create your views here.



# Create your views here.
def add_time_table(request):
    obj1=Department.objects.all()
    context={
        'xx':obj1
    }
    if request.method=='POST':
        obj=TimeTable()
        obj.department_id=request.POST.get('dept')
        myfile=request.FILES['timetable']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        obj.time_table=myfile.name
        # obj.time_table=request.POST.get('timetable')
        obj.save()
    return render(request,'time_table/time_table.html',context)

def view_time_table(request):
    obj = TimeTable.objects.all()
    context = {
        'x': obj,
    }
    return render(request,'time_table/view time_table.html',context)


def view_time_student(request):
    obj = TimeTable.objects.all()
    context = {
        'x': obj,
    }
    return render(request,'time_table/view_student.html',context)

