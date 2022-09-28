# Generated by Django 4.1.1 on 2022-09-28 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('d', '0012_rl_el_de_l_re_l'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='el',
            options={'ordering': ['la'], 'verbose_name': 'Entry Like'},
        ),
        migrations.AlterModelOptions(
            name='rl',
            options={'ordering': ['la'], 'verbose_name': 'Repost Like'},
        ),
        migrations.AddField(
            model_name='de',
            name='h',
            field=models.BooleanField(default=False, verbose_name='Archived?'),
        ),
        migrations.AddField(
            model_name='re',
            name='h',
            field=models.BooleanField(default=False, verbose_name='Archive?'),
        ),
        migrations.AlterField(
            model_name='de',
            name='l',
            field=models.ManyToManyField(blank=True, to='d.el'),
        ),
        migrations.AlterField(
            model_name='re',
            name='l',
            field=models.ManyToManyField(blank=True, to='d.rl'),
        ),
    ]