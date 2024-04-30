# Generated by Django 5.0.4 on 2024-04-25 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0010_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_id',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
