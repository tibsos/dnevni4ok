# Generated by Django 4.1.1 on 2022-09-22 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('u', '0010_b_uid_alter_p_b'),
        ('d', '0006_de_d'),
    ]

    operations = [
        migrations.CreateModel(
            name='RE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ca', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('ua', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('de', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='d.de')),
                ('p', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='u.p')),
            ],
        ),
    ]
