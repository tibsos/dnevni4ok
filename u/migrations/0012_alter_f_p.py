# Generated by Django 4.1.1 on 2022-09-27 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('u', '0011_f'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f',
            name='p',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following_profile', to='u.p', verbose_name='Followed Profile'),
        ),
    ]