# Generated by Django 2.2.2 on 2019-06-11 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_no_related_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='code',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
