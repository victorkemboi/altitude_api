from django.contrib import admin
from core.models import *

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_uuid','device_id','device_type')

admin.site.register(Device,DeviceAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id','name','mobile_number', 'email', 'userType',
    'userStatus','otp', 'device_id', 'user_id'
    )

admin.site.register(Customer,CustomerAdmin)

class AllianceAdmin(admin.ModelAdmin):
    list_display = ('alliance_id','name'
    )

admin.site.register(Alliance,AllianceAdmin)

class AirlineAdmin(admin.ModelAdmin):
    list_display = (
            'airline_id',
            'name',
            'website_link',
            'reservation_page_link',
            'frequent_flier_program_link',
            'alliance'
    )

admin.site.register(Airline,AirlineAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id','name','description'
    )

admin.site.register(Category,CategoryAdmin)

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('sub_category_id','name','description', 'category'
    )

admin.site.register(SubCategory,SubCategoryAdmin)

class MagazineAdmin(admin.ModelAdmin):
    list_display = (
            'magazine_id',
            'title',
            'publisher',
            'geographic_region',
            'category',
            'sub_category',
            'airline'
    )

admin.site.register(Magazine,MagazineAdmin)

class IssueAdmin(admin.ModelAdmin):
    list_display = (
            'issue_id',
            'title',
            'magazine',
            'issue_period',
            'cover_image_link',
            'pdf_file_link'
    )

admin.site.register(Issue,IssueAdmin)

class FavouriteMagazineAdmin(admin.ModelAdmin):
    list_display = (
            'favourite_mag_id',
            'magazine',
            'customer',
            'liked'
    )

admin.site.register(FavouriteMagazine,FavouriteMagazineAdmin)

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
            'subscription_id',
            'magazine',
            'customer',
            'subscription_type',
            'Amount',
            'subscription_date',
            'expiration_date',
            'payment_status',
            'auto_download'
    )

admin.site.register(Subscription,SubscriptionAdmin)

class IssueProgressAdmin(admin.ModelAdmin):
    list_display = (
            'issue_view_id',
            'issue',
            'customer',
            'current_progress',
            'max_progress',
            'is_downloaded'
    )

admin.site.register(IssueProgress,IssueProgressAdmin)

class FavouriteIssueAdmin(admin.ModelAdmin):
    list_display = (
            'favourite_issue_id',
            'issue',
            'customer',
            'liked'
    )

admin.site.register(FavouriteIssue,FavouriteIssueAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = (
            'payment_id',
            'subscription',
            'customer',
            'amount',
            'transaction_id',
            'transaction_type',
            'currency'
    )

admin.site.register(Payment,PaymentAdmin)
