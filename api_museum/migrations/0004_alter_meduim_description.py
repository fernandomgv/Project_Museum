# Generated by Django 4.0.5 on 2022-06-23 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_museum', '0003_alter_meduim_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meduim',
            name='description',
            field=models.CharField(max_length=200),
        ),
    ]
