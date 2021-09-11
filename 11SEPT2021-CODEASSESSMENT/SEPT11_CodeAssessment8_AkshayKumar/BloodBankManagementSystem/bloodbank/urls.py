from django.urls import path
from . import views

urlpatterns=[
  
    path('register/',views.registerDonor,name="registerDonor"),
    path('add/',views.addDonor,name="addDonor"),
    path('viewdonor/',views.viewAll,name="viewDonor"),
    path('home/',views.home,name='home'),
    path('login_check/',views.login_check),
    path('login/',views.login),
    path('view/',views.viewDonor),
    path('view/<id>',views.view,name='view'),
    path('update/',views.update_search,name="update_search"),
    path('update_data/',views.update_data,name='update_data'),
    path('updatedonor/',views.updateDonor,name='updateDonor'),
    
]