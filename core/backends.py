from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class EmailBackend(ModelBackend):
    user_model = get_user_model()
    def authenticate(self, request=None, username=None, password=None, **kwargs):
        response_user = None
        try:
            user = self.user_model.objects.get(username=username)
        except self.user_model.DoesNotExist:
           response_user = self.authenticate_email( username, password, **kwargs)
        else:
            if user.check_password(password):
                return user
        return response_user

    def authenticate_email(self, email=None, password=None, **kwargs):

        try:
            user = self.user_model.objects.get(email=email)
            
        except self.user_model.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None
