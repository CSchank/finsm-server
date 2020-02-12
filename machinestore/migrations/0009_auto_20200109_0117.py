# Generated by Django 3.0 on 2020-01-09 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machinestore', '0008_auto_20200109_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='machine_type',
            field=models.CharField(choices=[('D', 'DFA'), ('N', 'NFA'), ('P', 'NPDA'), ('T', 'Turing')], default='D', max_length=1),
        ),
    ]