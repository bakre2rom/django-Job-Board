# Generated by Django 3.2.7 on 2021-09-22 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='experience',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Part Time', 'Part Time'), ('Full Time', 'Full Time')], default='', max_length=15),
        ),
        migrations.AddField(
            model_name='job',
            name='published_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='vacancy',
            field=models.IntegerField(default=1),
        ),
    ]
