from django import forms
from .models import Report, Schedule


class ReportForm(forms.ModelForm):
    # schedule = forms.IntegerField(max_value=99999)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


    class Meta:
        model = Report
        fields = '__all__'
