# Generated by Django 2.2 on 2020-06-25 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_auto_20200625_1139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='modified_image',
        ),
    ]
