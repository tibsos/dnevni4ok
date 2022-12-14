# Generated by Django 4.1.1 on 2022-09-28 16:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('u', '0014_rename_pr_f_p'),
        ('d', '0015_ec_ecl_ec_l_ec_p'),
    ]

    operations = [
        migrations.CreateModel(
            name='RC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4)),
                ('c', models.TextField(max_length=300, verbose_name='Comment')),
                ('ca', models.DateTimeField(auto_now_add=True, verbose_name='Commented At')),
                ('ea', models.DateTimeField(auto_now=True, verbose_name='Edited At')),
                ('e', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='d.re', verbose_name='Diary Entry')),
                ('l', models.ManyToManyField(blank=True, to='d.ecl', verbose_name='Comment Likes')),
                ('p', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='u.p', verbose_name='Commenting Profile')),
                ('r', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='d.rc', verbose_name='Reply to comment')),
            ],
            options={
                'verbose_name': 'Entry Comment',
                'ordering': ['ca'],
            },
        ),
        migrations.AddField(
            model_name='ec',
            name='r',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='d.ec', verbose_name='Reply to comment'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='RCL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('la', models.DateTimeField(auto_now_add=True, verbose_name='Liked At')),
                ('e', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='d.rc', verbose_name='Comment')),
                ('p', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='u.p', verbose_name='Liking Profile')),
            ],
            options={
                'verbose_name': 'Repost Like',
                'ordering': ['la'],
            },
        ),
    ]
