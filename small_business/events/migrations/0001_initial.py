# Generated by Django 4.1.2 on 2022-10-29 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64, null=True, verbose_name='Customer First Name')),
                ('last_name', models.CharField(max_length=64, null=True, verbose_name='Customer Last Name')),
                ('email', models.EmailField(max_length=64, unique=True, verbose_name='Customer Email')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=16, null=True, verbose_name='Room Alias')),
                ('capacity', models.PositiveSmallIntegerField(unique=True, verbose_name='Capacity')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Event Name')),
                ('date', models.DateField(unique=True, verbose_name='Event Date')),
                ('time', models.TimeField(verbose_name='Event Time')),
                ('kind', models.CharField(choices=[('1', 'PRIVATE'), ('0', 'PUBLIC')], max_length=9)),
                ('description', models.TextField(blank=True)),
                ('attendees', models.ManyToManyField(blank=True, related_name='attendees', to='events.customer')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='event_room', to='events.room')),
            ],
        ),
    ]