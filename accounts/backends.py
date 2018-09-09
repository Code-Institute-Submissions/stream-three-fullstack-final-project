from .models import AllUser

## EMAIL AUTHENTICATION BACKEND ##

class EmailAuth:
  
    def authenticate(self, username=None, password=None):
        try:
            user = AllUser.objects.get(email=username)
            if user.check_password(password):
                return user
            return None

        except AllUser.DoesNotExist:
            return None

    def get_user(self, user_id):

        try:
            user = AllUser.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None

        except AllUser.DoesNotExist:
            return None