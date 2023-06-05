from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django_tables2 import SingleTableView

from .table import *
from .form import DriverEditForm, DriverRegisterForm


# Create your views here.

class Index(View):
    def get(self, request):
        return render(request, 'Manager/index.html')

    def post(self, request):
        user = None
        username = request.POST['username']
        password = request.POST['password']
        if username != "":
            try:
                user = Managers.objects.get(manager_id=username)
                if user.password == password:
                    print('mgr')
                else:
                    return render(request, 'Manager/index.html')
            except Managers.DoesNotExist:
                return render(request, 'Manager/index.html')
            if user is not None:
                # login(request, user)
                request.session['manager'] = user.manager_id
                return HttpResponse(f'login success{request.session["manager"]}')
        else:
            return render(request, 'Manager/index.html')


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
            context = self.get_context_data()
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
            context = self.get_context_data()
            return self.render_to_response(context)


class editDriver(View):

    def get(self, request, driver_id):
        if 'manager' in request.session:
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