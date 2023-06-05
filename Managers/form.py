from django import forms
from .models import Driver


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
