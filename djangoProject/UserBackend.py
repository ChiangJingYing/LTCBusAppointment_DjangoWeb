from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ValidationError
from .models import User, Managers, Driver


class CustomUserBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username)
            if user.password == password:
                return user
            print('user')
            raise ValidationError("user")
        except User.DoesNotExist:
            raise ValidationError("user")
        # return None




class CustomManagerBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            manager = Managers.objects.get(manager_id=username)
            if manager.password == password:
                return manager
            print('mgr')
            raise ValidationError("mgr")
        except Managers.DoesNotExist:
            raise ValidationError("mgr")
            # return None

        # return None
        # print("pass")



class CustomDriverBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            driver = Driver.objects.get(driver_id=username)
        except Managers.DoesNotExist:
            # raise PermissionDenied("adad")
            print('dri')

            return None
        else:
            if driver.password == password:
                return driver
        return None

        # raise PermissionDenied("adad")
