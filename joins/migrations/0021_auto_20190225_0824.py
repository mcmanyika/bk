# Generated by Django 2.1.5 on 2019-02-25 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0020_auto_20190225_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(blank=True, default='', null=True),
        ),
    ]
