# Generated by Django 3.1.1 on 2020-09-06 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemId', models.IntegerField()),
                ('ItemName', models.CharField(max_length=200)),
                ('Price', models.FloatField()),
                ('Quantity', models.IntegerField()),
                ('Category', models.CharField(max_length=200)),
            ],
        ),
    ]
