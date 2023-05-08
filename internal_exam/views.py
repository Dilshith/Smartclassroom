
from django.shortcuts import render
from internal_exam.models import InternalExam
from department.models import Department
import datetime

# Create your views here.
def post_internal_exam(request):
    obj=Department.objects.all()
    context={
        'x':obj,
    }
    if request.method == 'POST':
        obj = InternalExam()
        obj.department_id = request.POST.get('dname')
        obj.exam_subject = request.POST.get('exam_subject')
        obj.exam_id = request.POST.get('exam_id')
        # obj.date = datetime.datetime.now('date')
        # obj.time = datetime.datetime.now('time')
        selected_date = request.POST.get('date')
        selected_time = request.POST.get('time')
        date_obj = datetime.datetime.strptime(selected_date, '%Y-%m-%d').date()
        time_obj = datetime.datetime.strptime(selected_time, '%H:%M').time()
        obj.date = date_obj
        obj.time = time_obj

        obj.save()

    return render(request,'internal_exam/internal_exam.html',context)

def view_internal_exam(request):
    obj = InternalExam.objects.all()
    context = {
            'x': obj
    }
    return render(request,'internal_exam/view_internal_exam.html',context)
