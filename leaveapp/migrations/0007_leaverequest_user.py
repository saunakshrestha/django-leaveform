# Generated by Django 4.2.7 on 2023-11-20 06:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('leaveapp', '0001_squashed_0006_alter_leaverequest_leave_applied_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaverequest',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]