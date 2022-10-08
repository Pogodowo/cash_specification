from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.to_pdf,name='to_pdf'),

]