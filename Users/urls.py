from django.urls import path
from .views import *
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('logout', Logout.as_view(), name='logout'),
    path('register', Register.as_view(), name='register'),
    path('edit', EditInfo.as_view(), name='edit'),

    path('appointment_all', AppointmentTableView.as_view(), name='appointmentTable'),
]