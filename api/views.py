from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import JsonResponse
from rest_framework import viewsets, permissions, parsers, renderers
from api.serializers import *

# Create your views here.
class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    authentication_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        data = {
            'user_id': user.id,
            'username': user.username
        }
        

        data['token'] = token.key
        return JsonResponse(data)

class RegistrationView(APIView):
    authentication_classes = ''
    permission_classes = ''

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        resp ={}
        if serializer.is_valid():
            email_ = serializer.validated_data['email']
            try:
                user = User.objects.get(username=email_)
                user_serializer = UserSerializer(data=user)
                user_serializer.is_valid()
                return Response(user_serializer.data)
            except ObjectDoesNotExist:
                user = User.objects.create_user(username=email_, email=email_)
                user.set_password(serializer.validated_data['password'])
                user.save()

                if user.id:
                    device_id_ = serializer.validated_data['device_id']
                    device_type_ = serializer.validated_data['device_type']
                    device = Device.objects.create(device_id= device_id_, device_type=device_type_ )
                    device.save()
                    if device.device_uuid:

                        name_ = serializer.validated_data['name']
                        mobile_number_ = serializer.validated_data['mobile_number']
                        email_ = serializer.validated_data['email']
                        customer = Customer.objects.create(name=name_, mobile_number=mobile_number_,
                        email=email_, device=device, user=user)
                        customer.save()
                        resp = {

                            'user_id': customer.id,
                            'name': customer.name,
                            'email': customer.email,
                            'mobile_number': customer.mobile_number

                        }

        return Response(resp)

    def get(self, request):
        pass
