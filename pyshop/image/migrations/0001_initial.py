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
            name='Image',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('url', models.ImageField(upload_to='image')),
                ('alternative_text', models.CharField(max_length=100)),
                ('is_feature', models.BooleanField()),
                ('Inventory', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventory.inventory')),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
                'db_table': 'image',
            },
        ),
    ]
