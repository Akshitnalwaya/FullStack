from django.urls import path
from.import views

urlpatterns = [ 
    path("",views.index,name="index"),
    #            path("akshit",views.akshit,name="index"),
             path('hello/<str:name>', views.greet, name='greet')
                
               ]
