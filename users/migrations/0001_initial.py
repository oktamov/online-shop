# Generated by Django 4.2.2 on 2023-06-13 09:42

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phone_number', models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator('\\+?[1-9][0-9]{7,14}$', 'Enter a valid phone number')])),
                ('name', models.CharField(blank=True, max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VerificationCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6)),
                ('phone', models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator('\\+?[1-9][0-9]{7,14}$', 'Enter a valid phone number')])),
                ('verification_type', models.CharField(choices=[('register', 'Register'), ('login', 'Login')], max_length=50)),
                ('last_sent_time', models.DateTimeField(auto_now=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('expired_at', models.DateTimeField(null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='verification_codes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('phone', 'verification_type')},
            },
        ),
    ]
