# Generated by Django 5.0.6 on 2024-05-26 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=1000, null=True)),
                ('name', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
