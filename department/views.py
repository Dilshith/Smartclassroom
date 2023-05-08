from django.shortcuts import render

# Create your views here.
from department.models import Department

# Create your views here.
def add_department(request):
    if request.method=='POST':
        obj=Department()
        obj.department_id = request.POST.get('department_id')
        obj.department_name=request.POST.get('department')
        obj.save()
    return render(request,'department/department.html')

def view_department(request):
    obj=Department.objects.all()
    context={
        'x':obj,
    }
    return render(request,'department/view department.html',context)
