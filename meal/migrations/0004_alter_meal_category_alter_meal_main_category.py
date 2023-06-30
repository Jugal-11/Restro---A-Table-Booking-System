# Generated by Django 4.0.4 on 2022-04-24 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0003_administrative_finalbooked_tablebooking_tabledetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='category',
            field=models.CharField(choices=[('Fast Food', 'Fast Food'), ('Break Fast', 'Break Fast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner')], default='Select', max_length=30),
        ),
        migrations.AlterField(
            model_name='meal',
            name='main_category',
            field=models.CharField(choices=[('Veg', 'Veg Food'), ('Nonveg', 'Non Veg Food')], default='Select', max_length=30),
        ),
    ]
