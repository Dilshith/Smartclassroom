from django.conf.urls import url
from student import views
urlpatterns=[
    url('add_student/',views.post_student),
    url('view_student/',views.view_student),
    url('viewsadmn/', views.vsadmn),
    url('approvestudent/(?P<idd>\w+)',views.approve,name='ap'),
    url('rejectstudent/(?P<idd>\w+)',views.reject,name='rj'),
]