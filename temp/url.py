from django.conf.urls import url
from temp import views
urlpatterns=[
    url('home/',views.home, name='home'),
    url('admin/',views.admin),
    url('student/',views.student),
    url('teacher/',views.teacher, name='teacher'),

]