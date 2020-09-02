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