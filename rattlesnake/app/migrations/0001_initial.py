# Generated by Django 3.2.7 on 2021-09-02 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('identityNumber', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200, null=True)),
                ('department', models.CharField(max_length=200, null=True)),
                ('created_at' ,models.DateTimeField(auto_now_add=True)),
                ('updated_at ', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
