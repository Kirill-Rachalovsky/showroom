# Generated by Django 4.1 on 2022-08-15 11:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(help_text="<i>Put the car's brand</i>", max_length=50, verbose_name='Car Brand')),
                ('car_model', models.CharField(help_text="<i>Put the car's model</i>", max_length=50, verbose_name='Car Model')),
                ('description', models.TextField(blank=True, help_text='<i>More information about the car...</i>')),
                ('body_type', models.CharField(choices=[(None, 'Select the car body type'), ('SUV', 'SUV'), ('Sedan', 'Sedan'), ('Сoupe', 'Сoupe'), ('Wagon', 'Wagon'), ('Minivan', 'Minivan'), ('Hatchback', 'Hatchback'), ('Liftback', 'Liftback'), ('Limousine', 'Limousine'), ('Cabriolet', 'Cabriolet'), ('Another', 'Another')], max_length=50, verbose_name='Body type')),
                ('year', models.CharField(choices=[(1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], default=2022, max_length=50, verbose_name='Year')),
                ('transmission', models.CharField(choices=[(None, 'Select transmission type'), ('Manual', 'Manual'), ('Automatic', 'Automatic')], max_length=50, verbose_name='Transmission')),
                ('fuel', models.CharField(choices=[(None, 'Select fuel type'), ('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Gas', 'Gas'), ('Electric', 'Electric'), ('Hybrid', 'Hybrid')], max_length=50, verbose_name='Fuel type')),
                ('engine_capacity', models.FloatField(null=True, verbose_name='Engine capacity')),
                ('mileage', models.IntegerField(null=True, verbose_name='Car mileage')),
                ('is_new_car', models.BooleanField(default=False, verbose_name='New car')),
                ('color', models.CharField(choices=[(None, "Select car's color"), ('Red', 'Red'), ('Grey', 'Grey'), ('Light blue', 'Light blue'), ('Dark blue', 'Dark blue'), ('Green', 'Green'), ('Yellow', 'Yellow'), ('Pink', 'Pink'), ('Orange', 'Orange'), ('Brown', 'Brown'), ('White', 'White'), ('Black', 'Black'), ('Violet', 'Violet')], max_length=20, verbose_name='Color')),
                ('price', models.PositiveIntegerField(default=0, help_text='<i>Enter the price in dollars</i>', validators=[django.core.validators.MinValueValidator(0)], verbose_name='Price')),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
    ]
