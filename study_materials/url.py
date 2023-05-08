from django.conf.urls import url
from study_materials import views
urlpatterns = [
    url('add_study_materials/',views.post_study_materials),
    url('view_study_materials/',views.view_student_materials),
]



