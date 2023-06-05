from django.urls import path
from .views import *
urlpatterns = [
    path('', Index.as_view()),
    path('logout', Logout.as_view(), name='logoutdr'),
    path('schedule_table', ScheduleTable.as_view(), name='schedule_table'),
    path('report_form/<int:schedule_id>', ReportForm.as_view(), name='report_form'),
    path('route_table/<int:schedule_id>', RouteTableView.as_view(), name='route_table'),
]
