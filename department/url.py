from django.conf.urls import url
from department import views
urlpatterns=[
    url('add_department/',views.add_department),
    url('view_department/',views.view_department),
]