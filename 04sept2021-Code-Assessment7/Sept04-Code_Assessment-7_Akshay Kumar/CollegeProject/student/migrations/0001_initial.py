# Generated by Django 3.0.4 on 2021-08-28 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rollno', models.IntegerField()),
                ('admno', models.IntegerField()),
                ('college', models.CharField(max_length=50)),
                ('parent', models.CharField(max_length=50)),
                ('mobno', models.BigIntegerField()),
                ('dept', models.CharField(max_length=50)),
            ],
        ),
    ]
