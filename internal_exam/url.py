from django.conf.urls import url
from internal_exam import views
urlpatterns=[
    url('add_internal_exam/',views.post_internal_exam),
    url('view_internal_exam/',views.view_internal_exam),

]