# Generated by Django 4.0.2 on 2022-02-28 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mistapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sorev',
            old_name='Members',
            new_name='members',
        ),
        migrations.RenameField(
            model_name='sorev',
            old_name='Result',
            new_name='result',
        ),
    ]
