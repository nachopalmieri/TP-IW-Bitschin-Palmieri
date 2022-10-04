# Generated by Django 4.1 on 2022-09-20 19:04

from django.db import migrations, models
import tuneup.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tuneup', '0002_alter_adminuser_options_alter_baseuser_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='musichit',
            old_name='autor',
            new_name='author',
        ),
        migrations.AddField(
            model_name='musichit',
            name='state',
            field=models.TextField(choices=[('ACTIVE', 'Active'), ('IN_REVIEW', 'In Review'), ('DELETED', 'Deleted')], default='ACTIVE'),
        ),
        migrations.AlterField(
            model_name='musichit',
            name='audio',
            field=tuneup.models.fields.AudioFileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='musichit',
            name='cover',
            field=models.ImageField(upload_to='music_hits/covers/'),
        ),
    ]