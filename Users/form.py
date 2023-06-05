from django import forms
from .models import User


class UserRegisterForm(forms.ModelForm):
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

    def clean_username(self):
        username = self.cleaned_data.get('username')
        exist_username = [u.username for u in User.objects.raw("Select User_ID, Username From User")]
        if username in exist_username:
            raise forms.ValidationError('帳號已存在')
        return username

    class Meta:
        model = User
        exclude = ['auxiliary_tool']
        # fields = '__all__'

class UserEditForm(forms.ModelForm):
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
        model = User
        exclude = ['auxiliary_tool', 'username']
        # fields = '__all__'
