from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# Create your views here.
from study_materials.models import StudyMaterials
import datetime

# Create your views here.
def post_study_materials(request):
    if request.method=='POST':
        obj=StudyMaterials()
        obj.subject=request.POST.get('sub')
        obj.date=datetime.datetime.now()
        obj.time=datetime.datetime.now()
        myfile = request.FILES['material']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.study_material = myfile.name
        obj.save()
    return render(request,'study_materials/study_materials.html')

def view_student_materials(request):
    obj = StudyMaterials.objects.all()
    context = {
        'x': obj,
    }
    return render(request,'study_materials/view_study_materials.html',context)






































