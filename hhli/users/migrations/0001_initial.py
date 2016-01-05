# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-04 08:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('title', models.CharField(choices=[('MRS', 'Mrs'), ('MR', 'Mr'), ('DR', 'Dr'), ('OT', 'Others')], max_length=5)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other')], max_length=1)),
                ('date_of_birth', models.DateField(null=True)),
                ('height', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Circle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='name HUser can identify his group with', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='HUserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line_1', models.CharField(blank=True, max_length=50)),
                ('address_line_2', models.CharField(blank=True, max_length=50)),
                ('address_line_3', models.CharField(blank=True, max_length=50)),
                ('address_city', models.CharField(blank=True, max_length=30)),
                ('address_state', models.CharField(blank=True, max_length=30)),
                ('address_country', models.CharField(blank=True, max_length=30)),
                ('address_zip', models.CharField(blank=True, max_length=10)),
                ('contact_no', models.CharField(blank=True, max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('HUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Prospect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=25)),
                ('email_address', models.EmailField(max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
