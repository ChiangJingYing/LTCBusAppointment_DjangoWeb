from django.forms import ModelChoiceField

class ChoiseFieldShowCarNumber(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.car_number

class ChoiseFieldShowName(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name

class ChoiseFieldShowIDandDriverName(ModelChoiceField):
    def label_from_instance(self, obj):
        return f'{obj.id}: {obj.driver.name}({obj.vehicle.car_number})'