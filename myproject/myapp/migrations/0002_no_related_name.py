# Generated by Django 2.2.2 on 2019-06-11 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='client',
            field=models.ForeignKey(db_column='clientcode', on_delete=django.db.models.deletion.CASCADE, to='myapp.Client', to_field='code'),
        ),
    ]
