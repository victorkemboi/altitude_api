from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import viewsets, permissions, parsers, renderers, status
from api.serializers import *
from django.core.exceptions import ObjectDoesNotExist
from core.models import *
from rest_framework.authtoken.models import Token

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
        data = {}
        try:
            customer = Customer.objects.get(user=user)
            data['user_id'] = customer.customer_id
            data['name'] =customer.name
            data['email'] = customer.email
            data['mobile_number'] = customer.mobile_number
            data['token'] = token.key
        except ObjectDoesNotExist:
            pass
        
        return Response(data)

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

                            'user_id': customer.customer_id,
                            'name': customer.name,
                            'email': customer.email,
                            'mobile_number': customer.mobile_number

                        }

        return Response(resp)

    def get(self, request):
        pass

class CategoriesView(APIView):
    authentication_classes = ''
    permission_classes = ''

    def get(self, request):
        categories = Category.objects.all()
        categories_json = []
        for category in categories:
            categories_json.append(category.to_json())
        return Response(categories_json)

class SubCategoriesView(APIView):
    authentication_classes = ''
    permission_classes = ''

    def get(self, request):
        sub_categories = SubCategory.objects.all()
        sub_categories_json = []
        for sub_category in categories:
            sub_categories_json.append(category.to_json())
        return Response(categories_json)

class AirlinesView(APIView):
    authentication_classes = ''
    permission_classes = ''

    def get(self, request):
        airlines = Airline.objects.all()
        airlines_json = []
        for airline in airlines:
            airlines_json.append(airline.to_json())
        return Response(airlines_json)

class MagazinesView(APIView):
    authentication_classes = ''
    permission_classes = ''

    def post(self, request):
        serializer = MagazinesSerializer(data=request.data)
        get_by_ = serializer.validated_data['get_by']
        by_value_ = serializer.validated_data['by_value']
        newest_ = serializer.validated_data['newest']
        magazines_json = []
        #check if filter value set
        if by_value:
            #check filter_value group
            if get_by:
                if get_by == "geographic_region":
                    magazines = Magazine.objects.filter(geographic_region=by_value)
                    for magazine in magazines:
                       magazines_json.append(magazine.to_json()) 
                elif get_by == "airline":
                    magazines = Magazine.objects.filter(airline__airline_id=by_value)
                    for magazine in magazines:
                       magazines_json.append(magazine.to_json()) 
                elif get_by == "alliance":
                    magazines = Magazine.objects.filter(airline__alliance__alliance_id=by_value)
                    for magazine in magazines:
                       magazines_json.append(magazine.to_json()) 
                
                else:
                    pass
        else:
            magazines = Magazine.objects.all()

        return Response(magazines_json)

    def get(self, request):
        magazine_id = request.query_params['magazine_id']
        magazine = None
        try:
            magazine = Magazine.objects.get(magazine_id=magazine_id)
            return Response(magazine.to_json())
        except ObjectDoesNotExist:
            pass
        
        return Response(magazine, status=status.HTTP_404_NOT_FOUND)

class FavouriteMagazinesView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def post(self, request):
        serializer = AddFavouriteSerializer(data=request.data)
        user_id_ = serializer.validated_data['user_id']
        magazine_id_ = serializer.validated_data['magazine_id']
        like_status_ = serializer.validated_data['like_status']
        
        try:
            favourite_mag_record  = FavouriteMagazine.objects.get(customer__customer_id=user_id_,
            magazine__magazine_id = magazine_id_ )
            favourite_mag_record.liked = like_status_
            favourite_mag_record.save()
            return Response(favourite_mag_record.to_json())
        except ObjectDoesNotExist:
            try:
                customer  = Customer.objects.get(customer_id=user_id_)
                try:
                    magazine  = Magazine.objects.get(magazine_id=magazine_id_)
                    favourite_mag_record = FavouriteMagazine.objects.create(
                        magazine = magazine, customer = customer, liked =like_status_
                    )
                    favourite_mag_record.save()
                    return Response(favourite_mag_record.to_json())
                except ObjectDoesNotExist:
                    return Response(None, status=status.HTTP_404_NOT_FOUND) 
            except ObjectDoesNotExist:
                return Response(None, status=status.HTTP_404_NOT_FOUND) 

        return Response(None)    
    def get(self, request):
        customer_id = request.query_params['user_id']
        customer =None
        try:
            customer = Customer.objects.get(customer_id=customer_id)
        except ObjectDoesNotExist:
            pass
        favourite_magazines_json = []
        if customer:
            favourite_magazines = FavouriteMagazine.objects.filter(
                customer = customer, liked = True
            )
            for favourite_magazine in favourite_magazines:
                favourite_magazines_json.append(
                    favourite_magazine.magazine.to_json()
                )
        return Response(favourite_magazines_json)


class SubscriptionView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request):
        serializer = SubscriptionSerializer(data=request.data)
        user_id_ = serializer.validated_data['user_id']
        magazine_id_ = serializer.validated_data['magazine_id']
        subscription_type_ = serializer.validated_data['subscription_type']
        Amount_ = serializer.validated_data['Amount']
        subscription_date_ = serializer.validated_data['subscription_date']
        expiration_date_ = serializer.validated_data['expiration_date']
        payment_status_ = serializer.validated_data['payment_status']
        transaction_id_ = serializer.validated_data['transaction_id']
        transaction_type_ = serializer.validated_data['transaction_type']
        currency_ = serializer.validated_data['currency']

        customer = None
        try:
            customer = Customer.objects.get(customer_id=user_id_)
        except ObjectDoesNotExist:
            pass
        
        magazine = None
        try:
            magazine = Magazine.objects.get(magazine_id=magazine_id_)
        except ObjectDoesNotExist:
            pass
        
        if customer and magazine:
            subscription = Subscription.objects.create(
                magazine = magazine, 
                customer = customer,
                subscription_type = subscription_type_,
                amount = amount_,
                subscription_date = subscription_date_,
                expiration_date = expiration_date_,
                payment_status = payment_status_
            )

            subscription.save()

            payment = Payment.objects.create(
                subscription = subscription,
                customer = customer,
                amount = amount_,
                transaction_id = transaction_id_,
                transaction_type = transaction_type_,
                currency = currency_
            )
            payment.save()
    def get(self, request):
        customer_id = request.query_params['user_id']
        customer =None
        try:
            customer = Customer.objects.get(customer_id=customer_id)
        except ObjectDoesNotExist:
            pass
        subscriptions_json = []
        if customer:
            subscriptions = Subscription.objects.filter(
                customer = customer
            )
            for subscription in subscriptions:
                subscriptions_json.append(
                    subscription.magazine.to_json()
                )
        return Response(subscriptions_json)