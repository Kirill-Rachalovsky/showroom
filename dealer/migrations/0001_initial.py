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
        ('showroom', '0001_initial'),
        ('customer', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dealer',
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
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Dealer',
                'verbose_name_plural': 'Dealers',
            },
        ),
        migrations.CreateModel(
            name='DealerDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('amount', models.PositiveSmallIntegerField(help_text='How many cars do I need to buy for the discount?', validators=[django.core.validators.MinValueValidator(0)])),
                ('discount', models.PositiveIntegerField(default=0, help_text='Enter the size of the discount in percent', validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('data_start', models.DateField()),
                ('data_end', models.DateField(default=datetime.date(2022, 8, 20))),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.dealer')),
            ],
            options={
                'verbose_name': 'Discount',
                'verbose_name_plural': 'Discounts',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('brand', models.CharField(help_text="<i>Put the car's brand</i>", max_length=50, verbose_name='Car Brand')),
                ('car_model', models.CharField(help_text="<i>Put the car's model</i>", max_length=50, verbose_name='Car Model')),
                ('description', models.TextField(blank=True, help_text='<i>More information about the car...</i>')),
                ('body_type', models.IntegerField(choices=[(None, 'Select the car body type'), (1, 'SUV'), (2, 'Sedan'), (3, 'Сoupe'), (4, 'Wagon'), (5, 'Minivan'), (6, 'Hatchback'), (7, 'Liftback'), (8, 'Limousine'), (9, 'Cabriolet'), (10, 'Another')], verbose_name='Body type')),
                ('year', models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], default=2022, verbose_name='Year')),
                ('transmission', models.IntegerField(choices=[(None, 'Select transmission type'), (1, 'Manual'), (2, 'Automatic')], verbose_name='Transmission')),
                ('fuel', models.IntegerField(choices=[(None, 'Select fuel type'), (1, 'Petrol'), (2, 'Diesel'), (3, 'Gas'), (4, 'Electric'), (5, 'Hybrid')], verbose_name='Fuel type')),
                ('engine_capacity', models.FloatField(null=True, verbose_name='Engine capacity')),
                ('mileage', models.IntegerField(null=True, verbose_name='Car mileage')),
                ('is_new_car', models.BooleanField(default=False, verbose_name='New car')),
                ('color', models.IntegerField(choices=[(None, "Select car's color"), (1, 'Red'), (2, 'Grey'), (3, 'Light blue'), (4, 'Dark blue'), (5, 'Green'), (6, 'Yellow'), (7, 'Pink'), (8, 'Orange'), (9, 'Brown'), (10, 'White'), (11, 'Black'), (12, 'Violet')], verbose_name='Color')),
                ('price', models.PositiveIntegerField(default=0, help_text='<i>Enter the price in dollars</i>', validators=[django.core.validators.MinValueValidator(0)], verbose_name='Price')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customers_cars', to='customer.customer')),
                ('dealer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='dealers_cars', to='dealer.dealer')),
                ('showroom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='showrooms_cars', to='showroom.showroom')),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
    ]
