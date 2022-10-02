# Generated by Django 4.1.1 on 2022-10-02 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('attribute', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=100)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='attribute.attribute')),
            ],
            options={
                'verbose_name': 'attribute-value',
                'verbose_name_plural': 'attribute-values',
                'db_table': 'attribute-value',
            },
        ),
    ]