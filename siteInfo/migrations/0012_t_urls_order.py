# Generated by Django 2.2 on 2019-06-04 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteInfo', '0011_t_dictionary_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='t_urls',
            name='order',
            field=models.IntegerField(default=1),
        ),
    ]
