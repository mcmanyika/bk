# Generated by Django 2.2 on 2019-04-26 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='tracker',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='products.Category'),
        ),
    ]
