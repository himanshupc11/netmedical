# Generated by Django 3.1 on 2020-10-21 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netmedsapp', '0003_auto_20201019_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicines',
            name='genres',
            field=models.ManyToManyField(blank=True, null=True, related_name='Medicines', to='netmedsapp.medicine_type'),
        ),
    ]
