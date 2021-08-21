from django.urls import path
from . import views
import patients

urlpatterns = [
    path('',views.patients,name='patients'),
    path('add/',views.addPatients,name='addPatients'),
    path('viewall/',views.viewAll,name='viewAll'),
    path('view/<id>',views.view,name='view'),
    path('<pcode>/',views.viewpcode,name='viewpcode'),

]