from django.conf.urls import url
from chat import views

urlpatterns=[
    url('vc/',views.user),
    url('ad/(?P<idd>\w+)',views.adchat),
    url('std/',views.student),
    url('cus/(?P<idd>\w+)',views.cust),

]