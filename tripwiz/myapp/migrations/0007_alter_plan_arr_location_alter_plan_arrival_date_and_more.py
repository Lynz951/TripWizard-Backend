# Generated by Django 4.1.3 on 2022-12-06 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_plan_arr_location_alter_plan_arrival_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='arr_location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='arrival_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='dep_location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='departure_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='notes',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='room_info',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='ticket_info',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='vehicle_info',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
