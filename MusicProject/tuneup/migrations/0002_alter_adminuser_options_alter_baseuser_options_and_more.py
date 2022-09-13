# Generated by Django 4.1 on 2022-09-13 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuneup', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adminuser',
            options={'verbose_name': 'Admin User', 'verbose_name_plural': 'Admin Users'},
        ),
        migrations.AlterModelOptions(
            name='baseuser',
            options={'verbose_name': 'User', 'verbose_name_plural': 'All Users'},
        ),
        migrations.AlterModelOptions(
            name='standarduser',
            options={'verbose_name': 'Standard User', 'verbose_name_plural': 'Standard Users'},
        ),
        migrations.AlterField(
            model_name='baseuser',
            name='state',
            field=models.TextField(choices=[('ACTIVE', 'Active'), ('ACTIVE_UNVERIFIED', 'Active (Unverified)'), ('SUSPENDED', 'Suspended'), ('BLOQUED', 'Bloqued'), ('DELETED', 'Deleted')], default='ACTIVE_UNVERIFIED'),
        ),
    ]
