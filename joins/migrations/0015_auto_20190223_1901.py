# Generated by Django 2.1.5 on 2019-02-23 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0014_auto_20190223_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_acct',
            name='rootid',
            field=models.IntegerField(),
        ),
    ]
