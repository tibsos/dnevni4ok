# Generated by Django 4.1.1 on 2022-09-21 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('d', '0005_rename_p_d_a'),
    ]

    operations = [
        migrations.AddField(
            model_name='de',
            name='d',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='d.d'),
        ),
    ]