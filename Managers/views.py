from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django_tables2 import SingleTableView

from .table import *
from .form import DriverEditForm, DriverRegisterForm, AppointmentEditForm, ScheduleCreateForm


# Create your views here.

class Index(View):
    def get(self, request):
        if 'manager' in request.session:
            return render(request, 'Manager/base.html', {'logined': True})
        return render(request, 'Manager/index.html')

    def post(self, request):
        user = None
        username = request.POST['username']
        password = request.POST['password']
        if username != "":
            try:
                user = Managers.objects.get(manager_id=username)
                if user.password == password:
                    pass
                else:
                    error_message = '帳號密碼錯誤'
                    return render(request, 'Manager/index.html', locals())
            except Managers.DoesNotExist:
                error_message = '帳號密碼錯誤'
                return render(request, 'Manager/index.html', locals())
            if user is not None:
                # login(request, user)
                request.session['manager'] = user.manager_id
                return redirect('home')
        else:
            error_message = '帳號密碼錯誤'
            return render(request, 'Manager/index.html', locals())


class Logout(View):
    def get(self, request):
        if 'manager' in request.session:
            del request.session['manager']
        return redirect('/manager')


class UserAdminTableView(SingleTableView):
    table_class = UserTable
    template_name = 'Manager/user_table.html'

    def get_queryset(self, **kwargs):
        return User.objects.all().order_by('user_id')

    def get(self, request, *args, **kwargs):
        if 'manager' not in request.session or request.session['manager'] == '':
            return redirect('/manager')
        else:
            self.object_list = self.get_queryset()
            addition_data = {'logined': True}
            context = self.get_context_data(**addition_data)
            return self.render_to_response(context)


class editUser(View):
    def get(self, request, pk):
        return HttpResponse(pk)


class DriverAdminTableView(SingleTableView):
    table_class = DriverTable
    template_name = 'Manager/driver_table.html'

    def get_queryset(self, **kwargs):
        return Driver.objects.all().order_by('driver_id')

    def get(self, request, *args, **kwargs):
        if 'manager' not in request.session or request.session['manager'] == '':
            return redirect('/manager')
        else:
            self.object_list = self.get_queryset()
            addition_data = {'logined': True}
            context = self.get_context_data(**addition_data)
            return self.render_to_response(context)


class editDriver(View):

    def get(self, request, driver_id):
        if 'manager' in request.session:
            logined = True
            info = Driver.objects.raw("Select * from Driver Where Driver_ID = %s", [driver_id])
            form = DriverEditForm(instance=info[0])
            return render(request, 'Manager/edit_driver.html', locals())
        else:
            return redirect('/manager')

    def post(self, request, driver_id):
        info = Driver.objects.raw("Select * from Driver Where Driver_ID = %s", [driver_id])
        form = DriverEditForm(request.POST)
        if not form.is_valid():
            return render(request, 'Manager/edit_driver.html', locals())
        if len(info) > 0:
            form = DriverEditForm(request.POST, instance=info[0])
        form.save()
        return render(request, 'Manager/edit_driver.html', locals())


class registerDriver(View):
    def get(self, request):
        if 'manager' in request.session:
            logined = True
            init_data = {"manger": Managers.objects.filter(manager_id=request.session['manager'])[0]}
            form = DriverRegisterForm(initial=init_data)
            return render(request, 'Manager/registerDriver.html', locals())
        else:
            return redirect('/manager')

    def post(self, request):
        form = DriverRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/manager/mgdriver')
        else:
            return render(request, 'Manager/registerDriver.html', locals())


class HomePage(View):
    def get(self, request):
        if 'manager' in request.session:
            return render(request, 'Manager/home.html', {'logined': True})
        else:
            return redirect('/manager')


class StatisticsTableView(SingleTableView):
    table_class = StaticTable
    template_name = 'Manager/statistics_table.html'

    def get_queryset(self, **kwargs):
        return User.objects.raw(
            'SELECT User_ID, User.Username, COUNT(Appointment.Appointment_ID) AS appointment_times,\
             AVG(Appointment.Should_Pay) as avg_money\
             FROM User LEFT JOIN Appointment ON User.User_ID = Appointment.Appointment_User\
             GROUP BY User.User_ID, User.username;'
        )

    def get(self, request, *args, **kwargs):
        if 'manager' not in request.session or request.session['manager'] == '':
            return redirect('/manager')
        else:
            self.object_list = self.get_queryset()
            addition_data = {'logined': True}
            context = self.get_context_data(**addition_data)
            return self.render_to_response(context)


class AppointmentTableView(SingleTableView):
    table_class = AppointmentTable
    template_name = 'Manager/appointment_table.html'

    def get_queryset(self, **kwargs):
        form = Appointment.objects.raw(
            'Select * from Appointment')
        return form

    def get(self, request, *args, **kwargs):
        if 'manager' in request.session:
            tmp = {'logined': True}

            self.object_list = self.get_queryset()
            context = self.get_context_data(**tmp)
            return self.render_to_response(context)
        else:
            return redirect('/manager')


class EditAppointmentView(View):
    def get(self, request, appointment_id):
        if 'manager' in request.session:
            info = Appointment.objects.raw('Select * From Appointment Where Appointment_ID = %s', [appointment_id])
            form = AppointmentEditForm(instance=info[0])
            form.fields['schedules'].queryset = Schedule.objects.filter(date=info[0].date)
            form.initial['manager'] = Managers.objects.filter(manager_id=request.session['manager'])[0]
            return render(request, 'Manager/edit_appointment.html', locals())
        else:
            return redirect('manager')

    def post(self, request, appointment_id):
        form = AppointmentEditForm(request.POST)
        if form.is_valid():
            info = Appointment.objects.raw('Select * From Appointment Where Appointment_ID = %s', [appointment_id])
            form = AppointmentEditForm(request.POST, instance=info[0])
            form.save()
        else:
            return render(request, 'Manager/edit_appointment.html', locals())
        return redirect('/manager/mgappointment')


class ScheduleCreateView(View):
    def get(self, request):
        if 'manager' in request.session:
            form = ScheduleCreateForm()
            form.initial['manager'] = Managers.objects.filter(manager_id=request.session['manager'])[0]
            return render(request, 'Manager/create_schedule.html', locals())

    def post(self, request):
        form = ScheduleCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/manager/mgappointment')
        else:
            return redirect('/manager/mgappointment')
