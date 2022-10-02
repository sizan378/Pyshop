# Generated by Django 4.1.1 on 2022-10-02 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('is_active', models.BooleanField()),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categorys',
                'db_table': 'category',
            },
        ),
    ]
