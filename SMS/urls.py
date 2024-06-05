from django.urls import path
from . import views

urlpatterns = [
    path('sendotp/',views.Send_OTP),
    path('students/',views.Student_Data),
    path('login/',views.Login_Data),
    path('batches/',views.Batch_Data),
    path('dates/',views.Date_Data),
]
