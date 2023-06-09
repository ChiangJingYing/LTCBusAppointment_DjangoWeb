from django_tables2 import tables, Column
from .models import *


class Appointment(tables.Table):
    appointment_user = Column(accessor='appointment_user.username', verbose_name='預約帳號')
    manager = Column(accessor='manager.manager_id', verbose_name='客服ID')
    service_driver = Column(accessor='schedules.driver.name', verbose_name='服務司機')

    class Meta:
        model = Appointment
        attrs = {"class": "table table-striped table-sm text-nowrap"}
        exclude = ('appointment_id',)
        order_by = 'date'
