from django.shortcuts import render, redirect
from django.views.generic import View
from django_tables2 import SingleTableView

from .form import ReportForm as ReForm
from .models import Schedule, Report, Route, Driver
from .table import ScheduleTable as ST, RouteTable


# Create your views here.

class Index(View):
    def get(self, request):
        if 'driver' in request.session:
            return render(request, 'Driver/base.html', {'logined': True})
        return render(request, 'Driver/index.html')

    def post(self, request):
        user = None
        username = request.POST['username']
        password = request.POST['password']
        if username != "":
            try:
                user = Driver.objects.get(driver_id=username)
                if user.password == password:
                    pass
                else:
                    error_message = '帳號密碼錯誤'
                    return render(request, 'Driver/index.html', locals())
            except Driver.DoesNotExist:
                error_message = '帳號密碼錯誤'
                return render(request, 'Driver/index.html', locals())
            if user is not None:
                # login(request, user)
                request.session['driver'] = user.driver_id
                return redirect('schedule_table')
        else:
            error_message = '帳號密碼錯誤'
            return render(request, 'Driver/index.html', locals())



class Logout(View):
    def get(self, request):
        if 'driver' in request.session:
            del request.session['driver']
        return redirect('/driver')


class ScheduleTable(SingleTableView):
    table_class = ST
    template_name = 'Driver/schedule_table.html'

    def get_queryset(self, **kwargs):
        form = Schedule.objects.raw(
            'Select * from Schedule, Driver Where Schedule.Driver = Driver.Driver_ID and Schedule.Driver = %s order by Schedule.Date',
            [kwargs.get('user')])
        return form

    def get(self, request, *args, **kwargs):
        if 'driver' in request.session:
            self.object_list = self.get_queryset(user=request.session['driver'])
            addition_data = {
                'logined': True
            }
            context = self.get_context_data(**addition_data)
            return self.render_to_response(context)
        else:
            return redirect('/driver')


class ReportForm(View):
    def get(self, request, schedule_id):
        if 'driver' in request.session:
            logined = True
            init_data = {'schedule': Schedule.objects.filter(id=schedule_id)[0].id}
            old_data = Report.objects.raw("Select * from Report Where Schedule = %s", [schedule_id])
            if old_data:
                form = ReForm(instance=old_data[0])
            else:
                form = ReForm(initial=init_data)
            form.fields.items()
            return render(request, 'Driver/report_form.html', locals())
        else:
            return redirect('driver')

    def post(self, request, schedule_id):
        form = ReForm(request.POST)
        if not form.is_valid():
            return render(request, f'Driver/report_form.html', locals())
        info = Report.objects.raw("Select * from Report Where Schedule = %s", [form.cleaned_data.get('schedule').id])
        if info:
            form = ReForm(request.POST, instance=info[0])
        form.save()
        return redirect('/driver/schedule_table')


class RouteTableView(SingleTableView):
    table_class = RouteTable
    template_name = 'Driver/route_table.html'

    def get_queryset(self, **kwargs):
        form = Route.objects.raw("Select * From Route Where Schedule = %s Order By Time", [kwargs.get('schedule_id')])
        return form

    def get(self, request, schedule_id, *args, **kwargs):
        if 'driver' in request.session:
            self.object_list = self.get_queryset(schedule_id=schedule_id)
            addition_data = {
                'logined': True
            }
            context = self.get_context_data(**addition_data)
            return self.render_to_response(context)
        else:
            return redirect('/driver')
