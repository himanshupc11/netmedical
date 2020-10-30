# Generated by Django 3.1 on 2020-10-23 07:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('netmedsapp', '0004_auto_20201021_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL)),
                ('products', models.ManyToManyField(blank=True, null=True, related_name='cart', to='netmedsapp.Medicines')),
            ],
        ),
    ]
