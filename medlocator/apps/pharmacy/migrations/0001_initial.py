# Generated by Django 3.2.4 on 2021-07-06 23:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('pharmacy_name', models.CharField(max_length=250)),
                ('Account_manager_first_and_last_name', models.CharField(max_length=250)),
                ('email', models.EmailField(help_text='Required. Add a valid email', max_length=60)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Account_manager_phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('created_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pharmacy', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['pharmacy_name'],
            },
        ),
    ]