# Generated by Django 4.0.6 on 2022-07-21 13:59

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Showroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_creation', models.DateField(auto_now_add=True)),
                ('data_update', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('organization_name', models.CharField(max_length=50, unique=True, verbose_name='Organization Name')),
                ('description', models.TextField(blank=True, help_text='<i>More information about your company...</i>', verbose_name='Description')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('start_year', models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], default=2022, verbose_name='Year')),
                ('balance', models.PositiveIntegerField(default=0, help_text='<i>Put your balance in dollars</i>', verbose_name='Balance')),
                ('cars_options', models.JSONField(blank=True, null=True, verbose_name='Car priority')),
                ('price_increase', models.PositiveSmallIntegerField(default=30, help_text='<b>Enter the markup on the cars you sell</b>', validators=[django.core.validators.MaxValueValidator(500), django.core.validators.MinValueValidator(1)])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Showroom',
                'verbose_name_plural': 'Showrooms',
            },
        ),
        migrations.CreateModel(
            name='ShowroomDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('amount', models.PositiveSmallIntegerField(help_text='How many cars do I need to buy for the discount?', validators=[django.core.validators.MinValueValidator(0)])),
                ('discount', models.PositiveIntegerField(default=0, help_text='Enter the size of the discount in percent', validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('data_start', models.DateField()),
                ('data_end', models.DateField(default=datetime.date(2022, 8, 20))),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showroom.showroom')),
            ],
            options={
                'verbose_name': 'Discount',
                'verbose_name_plural': 'Discounts',
            },
        ),
    ]
