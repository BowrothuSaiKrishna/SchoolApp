from django.urls import path
from admissions.views import newadmission
from admissions.views import admissionreport
from admissions.views import addvendor
from admissions.views import deletedata
from admissions.views import updatedata
# Class based view
from admissions.views import firstclassbasedview, Teachersreport, Teacherdetails, addteacher, UpdateTeacher, removeteacher

urlpatterns = [
    path("newadm/", newadmission),
    path("admreport/", admissionreport),
    path("addvendor/", addvendor),
    path("delete/<int:id>", deletedata),
    path("update/<int:id>", updatedata),
    path("firstcbv/", firstclassbasedview.as_view()),
    path("tr/", Teachersreport.as_view(), name='listteachers'),
    path("td/<int:pk>/", Teacherdetails.as_view()),
    path("insertteacher/", addteacher.as_view()),
    path("insertteacher/", addteacher.as_view()),
    path("updateteacher/<int:pk>", UpdateTeacher.as_view()),
    path("removeteacher/<int:pk>", removeteacher.as_view()),
]
