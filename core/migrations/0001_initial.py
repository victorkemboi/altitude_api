# Generated by Django 2.2.16 on 2020-09-02 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alliance',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('alliance_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('mobile_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('userType', models.CharField(max_length=60)),
                ('userStatus', models.CharField(max_length=60)),
                ('otp', models.CharField(max_length=60)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('device_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('device_type', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('issue_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=60)),
                ('issue_period', models.CharField(max_length=60)),
                ('cover_image_link', models.CharField(max_length=120)),
                ('pdf_file_link', models.CharField(max_length=120)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('magazine_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=60)),
                ('publisher', models.CharField(max_length=60)),
                ('geographic_region', models.CharField(max_length=60)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('subscription_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('subscription_type', models.CharField(max_length=60)),
                ('Amount', models.FloatField()),
                ('subscription_date', models.DateField(auto_now=True)),
                ('expiration_date', models.DateField()),
                ('payment_status', models.CharField(max_length=60)),
                ('auto_download', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Customer')),
                ('magazine', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Magazine')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sub_category_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('payment_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.FloatField()),
                ('transaction_id', models.CharField(max_length=120)),
                ('transaction_type', models.CharField(max_length=60)),
                ('currency', models.CharField(max_length=60)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Customer')),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Subscription')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='magazine',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.SubCategory'),
        ),
        migrations.CreateModel(
            name='IssueView',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('issue_view_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('current_progress', models.CharField(max_length=60)),
                ('max_progress', models.CharField(max_length=60)),
                ('is_downloaded', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Customer')),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Issue')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='issue',
            name='magazine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Magazine'),
        ),
        migrations.CreateModel(
            name='FavouriteMagazine',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('favourite_mag_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('liked', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Customer')),
                ('magazine', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Magazine')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FavouriteIssue',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('favourite_issue_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('liked', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Customer')),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Issue')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('airline_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('website_link', models.CharField(max_length=120)),
                ('reservation_page_link', models.CharField(max_length=120)),
                ('frequent_flier_program_link', models.CharField(max_length=120)),
                ('alliance', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Alliance')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
