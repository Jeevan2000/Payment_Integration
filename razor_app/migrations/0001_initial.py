# Generated by Django 3.2.3 on 2021-07-24 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('paymentid', models.CharField(default='', max_length=300, null=True)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
    ]
