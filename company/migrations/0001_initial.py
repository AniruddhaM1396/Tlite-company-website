# Generated by Django 4.0.3 on 2022-11-06 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customerdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=50, null=True)),
            ],
        ),
    ]
