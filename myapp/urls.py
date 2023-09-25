from django.urls import path
from . import views



urlpatterns=[
    path('',views.api_data_view,name='index'),
    path('report',views.report,name='report'),
    path('bmi',views.bmi,name='bmi'),
    path('bodyfat',views.bodyfat,name='bodyfat'),
    path('calorie',views.calorie,name='calorie'),
    path('profile',views.profile,name='profile'),
 
    
]