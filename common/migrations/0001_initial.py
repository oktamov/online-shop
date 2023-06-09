# Generated by Django 4.2.2 on 2023-06-15 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('name_uz', models.CharField(max_length=100, null=True, verbose_name='Name')),
                ('name_ru', models.CharField(max_length=100, null=True, verbose_name='Name')),
                ('name_en', models.CharField(max_length=100, null=True, verbose_name='Name')),
                ('slug', models.CharField(blank=True, max_length=100, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Name')),
                ('title_uz', models.CharField(max_length=255, null=True, verbose_name='Name')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Name')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='Name')),
                ('slug', models.CharField(blank=True, max_length=255, unique=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_category', to='common.category')),
            ],
        ),
    ]
