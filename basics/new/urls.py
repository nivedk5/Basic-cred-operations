from django.urls import path,include
from new import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add',views.add,name='add'),
    path('addrec',views.addrec,name='addrec'),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('update/<int:id>/',views.update,name="update"),
    path('uprec/<int:id>/',views.update1,name="uprec"),
    
   
]