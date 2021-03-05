# Generated by Django 3.0.5 on 2020-04-18 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='contact',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='about_us',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='setting',
            name='email',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='setting',
            name='facebook',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='setting',
            name='fax',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='setting',
            name='instagram',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='setting',
            name='phone',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='setting',
            name='referances',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='smtp_email',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='setting',
            name='smtp_password',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='setting',
            name='smtp_port',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='setting',
            name='smtp_server',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='setting',
            name='twitter',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
