from django.urls import reverse
from django.utils.html import format_html
from django_tables2 import tables, Column
from .models import *


class ScheduleTable(tables.Table):
    actions = Column(empty_values=(), verbose_name='操作', orderable=False, exclude_from_export=True)
    driver = Column(accessor='driver.name')
    vehicle = Column(accessor='vehicle.car_number')
    manager = Column(accessor='manager.manager_id')

    def render_actions(self, value, record):
        return format_html(
            f'<a class="btn btn-sm badge badge-pill badge-warning" href={reverse("report_form", args=[str(record.pk)])}>回報</a>' +
            f'<a class="btn btn-sm badge badge-pill badge-info" href={reverse("route_table", args=[str(record.pk)])}>查看路線</a>'
        )

    class Meta:
        model = Schedule
        attrs = {"class": "table table-striped table-sm text-nowrap"}


class RouteTable(tables.Table):
    manager = Column(accessor='manager.manager_id', verbose_name='Managers ID')

    class Meta:
        model = Route
        attrs = {"class": "table table-striped table-sm text-nowrap"}
        exclude = ('schedule',)
