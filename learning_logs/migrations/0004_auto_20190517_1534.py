# Generated by Django 2.2.1 on 2019-05-17 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
