# Generated by Django 3.0.6 on 2020-05-12 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dcim', '0105_interface_name_collation'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OnboardingTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('group_id', models.CharField(blank=True, max_length=255)),
                ('ip_address', models.CharField(max_length=255, null=True)),
                ('username', models.CharField(blank=True, max_length=255)),
                ('password', models.CharField(blank=True, max_length=255)),
                ('secret', models.CharField(blank=True, max_length=255)),
                ('device_type', models.CharField(max_length=255, null=True)),
                ('status', models.CharField(max_length=255)),
                ('failed_reason', models.CharField(max_length=255, null=True)),
                ('message', models.CharField(blank=True, max_length=511)),
                ('port', models.PositiveSmallIntegerField(default=22)),
                ('timeout', models.PositiveSmallIntegerField(default=30)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dcim.Device')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('platform', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dcim.Platform')),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dcim.DeviceRole')),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dcim.Site')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]