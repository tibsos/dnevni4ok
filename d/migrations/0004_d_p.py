# Generated by Django 4.1.1 on 2022-09-19 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('u', '0004_p_a_p_b_p_n'),
        ('d', '0003_de_a_alter_f_aa_alter_f_f'),
    ]

    operations = [
        migrations.AddField(
            model_name='d',
            name='p',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='u.p'),
            preserve_default=False,
        ),
    ]