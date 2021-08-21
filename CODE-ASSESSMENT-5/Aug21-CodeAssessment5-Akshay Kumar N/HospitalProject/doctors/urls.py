from django.urls import path
from doctors import views

urlpatterns = [
    path('',views.doctors,name='doctors'),
    path('register/',views.doclogin,name='doclogin'),
    path('add/',views.addDoctor,name='addDoctor'),
    path('viewall/',views.viewAll,name='viewAll'),
    path('view/<id>',views.view,name='view'),
    path('<dcode>/',views.viewdcode,name='viewdcode'),

]