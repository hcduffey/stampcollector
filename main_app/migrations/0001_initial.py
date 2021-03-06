# Generated by Django 4.0.4 on 2022-06-01 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
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
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stamps', to='main_app.collection')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
