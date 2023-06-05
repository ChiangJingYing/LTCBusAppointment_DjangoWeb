from django_tables2 import tables, Column
from django.utils.html import format_html
from django.urls import reverse
from .models import *


class UserTable(tables.Table):
    actions = Column(empty_values=(), verbose_name='操作', orderable=False, exclude_from_export=True)
    auxiliary_tool_id = Column(accessor='auxiliary_tool.tool_id', verbose_name='輔具ID')
    auxiliary_tool_name = Column(accessor='auxiliary_tool.tool_name', verbose_name='輔具名稱')
    auxiliary_tool_min_size = Column(accessor='auxiliary_tool.min_size', verbose_name='最小尺寸')

    class Meta:
        model = User
        attrs = {"class": "table table-striped table-sm text-nowrap"}
        exclude = ('auxiliary_tool',)
        sequence = [col.name for col in User._meta.fields]
        sequence += ['auxiliary_tool_id', 'auxiliary_tool_name', 'auxiliary_tool_min_size']

    def render_actions(self, value, record):
        return format_html(
            f'<a class="btn btn-sm badge badge-pill badge-warning" href="{reverse("editUser", args=[str(record.pk)])}">編輯</a>'
        )


class DriverTable(tables.Table):
    actions = Column(empty_values=(), verbose_name='操作', orderable=False, exclude_from_export=True)
    manger = Column(accessor='manger.manager_id', verbose_name="Manager ID")
    class Meta:
        model = Driver
        attrs = {"class": "table table-striped table-sm text-nowrap"}

    def render_actions(self, value, record):
        return format_html(
            f'<a class="btn btn-sm badge badge-pill badge-warning" href={reverse("editDriver", args=[str(record.pk)])}>編輯</a>'
        )
