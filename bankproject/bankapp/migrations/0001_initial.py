# Generated by Django 4.2.4 on 2023-08-06 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField()),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('account_type', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
            ],
        ),
    ]
