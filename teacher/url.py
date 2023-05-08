from django.conf.urls import url
from teacher import views
urlpatterns = [
    url('add_teacher/',views.add_teacher),
    url('view_teacher/',views.view_teacher),
    url('approveteacher/(?P<idd>\w+)',views.approve,name='app'),
    url('rejectteacher/(?P<idd>\w+)',views.reject,name='rje'),
]





