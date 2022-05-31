# Generated by Django 4.0.4 on 2022-05-30 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stamp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('condition', models.CharField(choices=[('U', 'Used'), ('N', 'New')], default='New', max_length=15)),
                ('centering', models.CharField(max_length=100)),
                ('format', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]