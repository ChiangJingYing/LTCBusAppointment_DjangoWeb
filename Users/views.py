from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django_tables2 import SingleTableView

from .form import UserRegisterForm, UserEditForm, AppointmentCreateForm
from .models import User, Appointment
from .table import Appointment as AppointmentTable


# Create your views here.

class Index(View):
    def get(self, request):
        if 'user' in request.session:
            return render(request, 'User/base.html', {'logined': True})
        return render(request, 'User/index.html')

    def post(self, request):
        user = None
        username = request.POST['username']
        password = request.POST['password']
        if username != "":
            try:
                user = User.objects.get(username=username)
                if user.password == password:
                    pass
                else:
                    error_message = '帳號密碼錯誤'
                    return render(request, 'User/index.html', locals())
            except User.DoesNotExist:
                error_message = '帳號密碼錯誤'
                return render(request, 'User/index.html', locals())
            if user is not None:
                request.session['user'] = user.username
                return render(request, 'User/base.html', {'logined': True})
        else:
            error_message = '帳號密碼錯誤'
            return render(request, 'User/index.html', locals())


class Logout(View):
    def get(self, request):
        if 'user' in request.session:
            del request.session['user']
        return redirect('/user')


class Register(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'User/register.html', locals())

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if not form.is_valid():
            return render(request, 'User/register.html', locals())
        form.save()
        return redirect('/user')


class EditInfo(View):
    def get(self, request):
        if 'user' in request.session:
            logined = True
            username = request.session['user']
            info = User.objects.raw("Select * from User Where Username=%s", [username])
            form = UserEditForm(instance=info[0])
            return render(request, 'User/edit.html', locals())
        else:
            return redirect('/user')

    def post(self, request):
        username = request.session['user']
        info = User.objects.raw("Select * from User Where Username=%s", [username])
        form = UserEditForm(request.POST)
        if not form.is_valid():
            return render(request, 'User/register.html', locals())
        form = UserEditForm(request.POST, instance=info[0])
        form.save()
        return render(request, 'User/edit.html', locals())


class AppointmentTableView(SingleTableView):
    table_class = AppointmentTable
    template_name = 'User/appointment_table.html'

    def get_queryset(self, **kwargs):
        form = Appointment.objects.raw(
            'Select * from Appointment, User WHERE Appointment.Appointment_User = User.User_ID and User.Username = %s',
            [kwargs.get('user')])
        return form

    def get(self, request, *args, **kwargs):
        if 'user' in request.session:
            tmp = {'logined': True}

            self.object_list = self.get_queryset(user=request.session['user'])
            context = self.get_context_data(**tmp)
            return self.render_to_response(context)
        else:
            return redirect('/user')


class AppointmentCreateView(View):
    def get(self, request):
        if 'user' in request.session:
            show_field = ['Type', 'Date', 'Escorts', 'Destination']
            data = {
                'appointment_user': User.objects.filter(username=request.session['user'])[0],
                'status': '待排班'
            }
            form = AppointmentCreateForm(initial=data)
            return render(request, 'User/Appointment_create.html', locals())
        else:
            return redirect('user')

    def post(self, request):
        form = AppointmentCreateForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'User/Appointment_create.html', locals())
        return redirect('/user/appointment_all')
