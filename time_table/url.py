from django.conf.urls import url
from time_table import views
urlpatterns=[
    url('add_time_table/',views.add_time_table),
    url('teacher_vw/',views.view_time_table),
    url('stdvw/', views.view_time_student)
]