# Generated by Django 3.1.3 on 2020-11-17 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='star',
            field=models.CharField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], max_length=10),
        ),
    ]
