# Generated by Django 3.2.3 on 2021-06-16 13:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('business_projects', '0001_initial'),
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmodel',
            name='employess',
            field=models.ManyToManyField(to='users.EmployModel'),
        ),
        migrations.AddField(
            model_name='projectmodel',
            name='inventory',
            field=models.ManyToManyField(to='business_projects.InventoryModel'),
        ),
        migrations.AddField(
            model_name='projectmodel',
            name='supplies',
            field=models.ManyToManyField(to='business_projects.SupplyModel'),
        ),
        migrations.AddField(
            model_name='inventorymodel',
            name='products',
            field=models.ManyToManyField(to='business_projects.ProductModel'),
        ),
        migrations.AddField(
            model_name='historicalsupplymodel',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalprojectmodel',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalproductmodel',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalinventorymodel',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
