# Generated by Django 3.0.5 on 2020-04-25 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paint', '0016_auto_20200424_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivers',
            name='Delivery_status',
            field=models.CharField(choices=[('DELIVERED', 'DELIVERED'), ('NOT DELIVERED', 'NOT DELIVERED')], max_length=50, verbose_name='Delivery Status'),
        ),
        migrations.AlterField(
            model_name='purchase_consists_of',
            name='Purchase_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='paint.Purchase', verbose_name='Purchase ID'),
        ),
    ]
