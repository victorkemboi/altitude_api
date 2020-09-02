from django.db import models
from django.contrib.auth.models import User
import uuid

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Device(models.Model):
    device_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    device_id = models.CharField(max_length=60)
    device_type = models.CharField(max_length=60)

    def to_json(self):
        return {
            'device_uuid':self.device_uuid,
            'device_id':self.device_id,
            'device_type':self.device_type
        }

    def __str__(self):
        return self.device_type

class Customer(BaseModel):
    customer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    mobile_number = models.CharField(max_length=20)
    email = models.EmailField()
    userType = models.CharField(max_length=60, null=True)
    userStatus = models.CharField(max_length=60, null=True)
    otp = models.CharField(max_length=60, null=True)
    device = models.ForeignKey(Device,  on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User,  on_delete=models.CASCADE)

    def to_json(self):
        return{
            'customer_id':self.customer_id,
            'name':self.name,
            'mobile_number':self.mobile_number,
            'email':self.email,
            'userType':self.userType,
            'userStatus':self.userStatus,
            'otp':self.otp,
            'device_id': self.device.device_id,
            'user_id':self.user.id
            
        }

    def __str__(self):
        return self.name 

class Alliance(BaseModel):
    alliance_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=60)   

    def to_json(self):
        return{
            'alliance_id':self.alliance_id,
            'name':self.name
        }

    def __str__(self):
        return self.name

class Airline(BaseModel):
    airline_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=60)   
    website_link = models.CharField(max_length=120) 
    reservation_page_link = models.CharField(max_length=120) 
    frequent_flier_program_link = models.CharField(max_length=120) 
    alliance = models.ForeignKey(Alliance,  on_delete= models.DO_NOTHING)

    def to_json(self):
        return{
            'airline_id':self.airline_id,
            'name':self.name,
            'website_link':self.website_link,
            'reservation_page_link':self.reservation_page_link,
            'frequent_flier_program_link':self.frequent_flier_program_link,
            'alliance_id':self.alliance.alliance_id
        }

    def __str__(self):
        return self.name

class Category(BaseModel):
    category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=60) 
    description = models.CharField(max_length=100) 

    def to_json(self):
        return{
            'category_id':self.category_id,
            'name':self.name,
            'description':self.description
        }

    def __str__(self):
        return self.name

class SubCategory(BaseModel):
    sub_category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=60) 
    description = models.CharField(max_length=100) 
    category = models.ForeignKey(Category,  on_delete= models.DO_NOTHING)

    def to_json(self):
        return{
            'sub_category_id':self.sub_category_id,
            'name':self.name,
            'description':self.description,
            'category_id':self.category.category_id,
        }

    def __str__(self):
        return self.name

class Magazine(BaseModel):
    magazine_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=60)
    publisher = models.CharField(max_length=60)
    geographic_region = models.CharField(max_length=60)
    category = models.ForeignKey(Category,  on_delete=models.DO_NOTHING)
    sub_category = models.ForeignKey(SubCategory,  on_delete=models.DO_NOTHING)
    airline = models.ForeignKey(Airline,default=uuid.uuid4,  on_delete=models.DO_NOTHING)

    def to_json(self):
        return{
            'magazine_id':self.magazine_id,
            'title':self.title,
            'publisher':self.publisher,
            'geographic_region':self.geographic_region,
            'category_id':self.category.category_id,
            'sub_category_id':self.sub_category.sub_category_id,
            'airline_id': self.airline.airline_id
        }

    def __str__(self):
        return self.title

class Issue(BaseModel):
    issue_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=60)
    magazine = models.ForeignKey(Magazine,  on_delete=models.DO_NOTHING)
    issue_period = models.CharField(max_length=60)
    cover_image_link = models.CharField(max_length=120)
    pdf_file_link = models.CharField(max_length=120)

    def to_json(self):
        return{
            'issue_id':self.issue_id,
            'title':self.title,
            'magazine_id':self.magazine.magazine_id,
            'issue_period':self.issue_period,
            'cover_image_link':self.cover_image_link,
            'pdf_file_link':self.pdf_file_link
        }

    def __str__(self):
        return self.title


class Subscription(BaseModel):
    subscription_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    magazine = models.ForeignKey(Magazine,  on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customer,  on_delete=models.DO_NOTHING)
    subscription_type = models.CharField(max_length=60)
    Amount = models.FloatField()
    subscription_date = models.DateField(auto_now = True)
    expiration_date = models.DateField()
    payment_status = models.CharField(max_length=60)
    auto_download = models.BooleanField(default=False)

    def to_json(self):
        return{
            'subscription_id':self.subscription_id,
            'magazine_id':self.magazine.magazine_id,
            'customer_id':self.customer_id,
            'subscription_type':self.subscription_type,
            'Amount':self.Amount,
            'subscription_date':self.subscription_date,
            'expiration_date':self.expiration_date,
            'payment_status':self.payment_status,
            'auto_download':self.auto_download,
        }

    def __str__(self):
        return self.subscription_type

class IssueView(BaseModel):
    issue_view_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    issue = models.ForeignKey(Issue,  on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customer,  on_delete=models.DO_NOTHING)
    current_progress = models.CharField(max_length=60)
    max_progress = models.CharField(max_length=60)
    is_downloaded = models.BooleanField(default=False)

    def to_json(self):
        return{
            'issue_view_id':self.issue_view_id,
            'issue_id':self.issue.issue_id,
            'customer_id':self.customer.customer_id,
            'current_progress':self.current_progress,
            'max_progress':self.max_progress,
            'is_downloaded':self.is_downloaded
        }

    def __str__(self):
        return self.issue_view_id

class FavouriteMagazine(BaseModel):
    favourite_mag_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    magazine = models.ForeignKey(Magazine,  on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customer,  on_delete=models.DO_NOTHING)
    liked = models.BooleanField(default=False)

    def to_json(self):
        return{
            'favourite_mag_id':self.favourite_mag_id,
            'magazine_id':self.magazine.magazine_id,
            'customer_id':self.customer_id,
            'liked':self.liked,
        }

    def __str__(self):
        return self.favourite_mag_id

class FavouriteIssue(BaseModel):
    favourite_issue_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    issue = models.ForeignKey(Issue,  on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customer,  on_delete=models.DO_NOTHING)
    liked = models.BooleanField(default=False)

    def to_json(self):
        return{
            'favourite_issue_id':self.favourite_issue_id,
            'issue_id':self.issue.issue_id,
            'customer_id':self.customer_id,
            'liked':self.liked,
        }

    def __str__(self):
        return self.favourite_issue_id

class Payment(BaseModel):
    payment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subscription = models.ForeignKey(Subscription,  on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customer,  on_delete=models.DO_NOTHING)
    amount = models.FloatField()
    transaction_id = models.CharField(max_length=120)
    transaction_type = models.CharField(max_length=60)
    currency = models.CharField(max_length=60)

    def to_json(self):
        return{
            'payment_id':self.payment_id,
            'subscription_id':self.subscription.subscription_id,
            'customer_id':self.customer.customer_id,
            'amount':self.amount,
            'transaction_id':self.transaction_id,
            'transaction_type':self.transaction_type,
            'currency':self.currency
        }

    def __str__(self):
        return self.amount