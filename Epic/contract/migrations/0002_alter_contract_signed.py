# Generated by Django 4.1.3 on 2022-11-24 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='signed',
            field=models.BooleanField(null=True),
        ),
    ]
