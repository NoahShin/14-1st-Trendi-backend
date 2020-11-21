# Generated by Django 3.1.3 on 2020-11-20 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('hash_tag', models.TextField(null=True)),
                ('image_url', models.URLField(max_length=1000)),
            ],
            options={
                'db_table': 'sellers',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nick_name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=100)),
                ('user_name', models.CharField(max_length=100, null=True)),
                ('phone_number', models.CharField(max_length=20, null=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
