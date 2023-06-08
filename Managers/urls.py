from django.urls import path
from .views import *
urlpatterns = [
    path('', Index.as_view()),
    path('home', HomePage.as_view(), name='home'),
    path('logoutMgr', Logout.as_view(), name='logoutmgr'),
    path('mguser', UserAdminTableView.as_view(), name='mguser'),
    path('mgdriver', DriverAdminTableView.as_view(), name='mgdriver'),
    path('mgappointment', AppointmentTableView.as_view(), name='mgappointment'),

    path('statistic', StatisticsTableView.as_view(), name='statistic'),

    path('editUser/<int:pk>', editUser.as_view(), name='editUser'),
    path('editDriver/<int:driver_id>', editDriver.as_view(), name='editDriver'),
    path('editAppointment/<int:appointment_id>', EditAppointmentView.as_view(), name='editAppointment'),
    path('registerDriver', registerDriver.as_view(), name='registerDriver'),
]