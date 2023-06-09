from django import forms
from .models import Driver, Appointment, Schedule


class DriverEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Driver
        exclude = ['manger']


class DriverRegisterForm(forms.ModelForm):
    check_password = forms.CharField(max_length=40)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

    def clean_check_password(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('check_password')
        if password != password2:
            raise forms.ValidationError('兩次密碼不相同')

    class Meta:
        model = Driver
        fields = '__all__'


class AppointmentEditForm(forms.ModelForm):

    def clean_escorts(self):
        data = self.cleaned_data.get('escorts')
        if data and data < 0:
            raise forms.ValidationError('陪同人數不可小於0')
        if not data:
            return 0
        return data

    def clean_mileage(self):
        data = self.cleaned_data.get('mileage')
        if data and data < 0:
            raise forms.ValidationError('搭乘里程不可小於0')
        if not data:
            return 0
        return data

    def clean_should_pay(self):
        data = self.cleaned_data.get('should_pay')
        if data and data < 0:
            raise forms.ValidationError('應付金額不可小於0')
        return data

    class Meta:
        model = Appointment
        fields = '__all__'
