# Generated by Django 2.0.5 on 2018-06-03 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getlatex', '0002_auto_20180603_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='latexexpr',
            name='accesses',
            field=models.BigIntegerField(default=0, verbose_name='number of accesses'),
        ),
        migrations.AlterField(
            model_name='latexexpr',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='latexexpr',
            name='expression',
            field=models.CharField(max_length=256, verbose_name='LaTeX Expression'),
        ),
        migrations.AlterField(
            model_name='latexexpr',
            name='svg_data',
            field=models.TextField(default='', verbose_name='SVG Data'),
        ),
    ]