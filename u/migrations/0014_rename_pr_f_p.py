# Generated by Django 4.1.1 on 2022-09-27 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('u', '0013_rename_p_f_pr'),
    ]

    operations = [
        migrations.RenameField(
            model_name='f',
            old_name='pr',
            new_name='p',
        ),
    ]