# Generated by Django 5.0.4 on 2024-06-03 03:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('restaurants', '0001_initial'),
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='waiter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.waiter'),
        ),
        migrations.AddField(
            model_name='bill',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restaurants.order'),
        ),
        migrations.AddField(
            model_name='products_order',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restaurants.order'),
        ),
        migrations.AddField(
            model_name='products_order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.product'),
        ),
        migrations.AddField(
            model_name='products_restaurant',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.product'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='products_restaurant',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restaurants.restaurant'),
        ),
        migrations.AddField(
            model_name='tables_restaurant',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restaurants.restaurant'),
        ),
        migrations.AddField(
            model_name='tables_restaurant',
            name='table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restaurants.table'),
        ),
        migrations.AddField(
            model_name='order',
            name='table_restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restaurants.tables_restaurant'),
        ),
        migrations.AddField(
            model_name='tip_waiter',
            name='bill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restaurants.bill'),
        ),
        migrations.AddField(
            model_name='tip_waiter',
            name='waiter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.waiter'),
        ),
        migrations.AddField(
            model_name='waiter_shift',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restaurants.restaurant'),
        ),
        migrations.AddField(
            model_name='waiter_shift',
            name='waiter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.waiter'),
        ),
    ]