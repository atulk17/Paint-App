# Generated by Django 3.0.5 on 2020-04-25 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paint', '0018_auto_20200425_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase_consists_of',
            name='Purchase_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='paint.Purchase', verbose_name='Purchase ID'),
        ),
    ]
