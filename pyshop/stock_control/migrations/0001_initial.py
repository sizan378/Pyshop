# Generated by Django 4.1.1 on 2022-10-02 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockControl',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('unit', models.IntegerField()),
                ('last_checked', models.DateTimeField()),
                ('Inventory', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='inventory.inventory')),
            ],
            options={
                'verbose_name': 'stock',
                'verbose_name_plural': 'stocks',
                'db_table': 'stock',
            },
        ),
    ]