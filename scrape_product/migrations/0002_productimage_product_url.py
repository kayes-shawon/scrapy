# Generated by Django 3.1.4 on 2022-05-22 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrape_product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='product_url',
            field=models.CharField(default='', max_length=250, verbose_name='Product url'),
        ),
    ]
