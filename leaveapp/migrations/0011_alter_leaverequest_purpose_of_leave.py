# Generated by Django 4.2.7 on 2023-11-30 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaveapp', '0010_alter_leaverequest_purpose_of_leave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaverequest',
            name='purpose_of_leave',
            field=models.CharField(choices=[('annual_leave', 'Annual Leave'), ('sick_leave', 'Sick Leave'), ('bereavement_leave', 'Bereavement Leave'), ('maternity_leave', 'Maternity Leave'), ('paternity_leave', 'Paternity Leave'), ('others', 'Others')], max_length=50),
        ),
    ]
