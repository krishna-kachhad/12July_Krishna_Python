from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index),
    path('showdata/',views.showdata,name='showdata'),
    path('updatedata/<int:id>',views.updatedata),
    path('deletedata/<int:id>',views.deletedata),
]