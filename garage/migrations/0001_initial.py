# Generated by Django 5.1.3 on 2024-11-14 20:32

import django.core.validators
import django.db.models.deletion
import django.db.models.functions.text
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('colour', models.CharField(help_text='Enter a colour for the car', max_length=200)),
                ('year', models.CharField(max_length=4, validators=[django.core.validators.MinLengthValidator(4)])),
                ('VIN', models.CharField(max_length=17, unique=True, validators=[django.core.validators.MinLengthValidator(17)])),
                ('mileage', models.IntegerField()),
                ('status', models.CharField(blank=True, choices=[('a', 'Available'), ('u', 'Unavailable'), ('m', 'Maintenance')], default='a', max_length=1)),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='garage.carmodel')),
            ],
        ),
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a car make (e.g. Nissan, Honda, Toyota etc.)', max_length=200, unique=True)),
            ],
            options={
                'constraints': [models.UniqueConstraint(django.db.models.functions.text.Lower('name'), name='make_name_case_insensitive_unique', violation_error_message='Make already exists')],
            },
        ),
        migrations.AddField(
            model_name='carmodel',
            name='make',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='garage.make'),
        ),
    ]
