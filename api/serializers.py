from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _
from core.backends import EmailBackend
from django.contrib.auth.models import User
from core.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

class MagazineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magazine
        fields = '__all__'

class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(label=_("email"))
    password = serializers.CharField(label=_("Password"), style={'input_type': 'password'})

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            backend = EmailBackend()
            user = backend.authenticate(username=email, password=password)
            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise serializers.ValidationError(msg)
            else:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg)
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg)

        attrs['user'] = user
        return attrs

class RegistrationSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    device_id = serializers.CharField()
    device_type = serializers.CharField()
    mobile_number = serializers.CharField()

class MagazinesSerializer(serializers.Serializer):
    get_by = serializers.CharField(default=None, allow_blank=True)
    by_value = serializers.CharField(default=None, allow_blank=True)
    newest = serializers.CharField(default=None, allow_blank=True)

class AddFavouriteSerializer(serializers.Serializer):
    user_id = serializers.CharField()
    magazine_id = serializers.CharField()
    like_status = serializers.BooleanField(default=False)

class SubscriptionSerializer(serializers.Serializer):
    magazine_id = serializers.CharField()
    user_id = serializers.CharField()
    subscription_type = serializers.CharField()
    Amount = serializers.FloatField()
    subscription_date = serializers.DateField()
    expiration_date = serializers.DateField()
    payment_status = serializers.CharField()
    transaction_id = serializers.BooleanField()
    transaction_type = serializers.CharField()
    currency = serializers.CharField()

class IssueProgressSerializer(serializers.Serializer):
    issue_id = serializers.CharField()
    user_id = serializers.CharField()
    current_progress = serializers.CharField()
    max_progress = serializers.CharField()
    is_downloaded = serializers.CharField()