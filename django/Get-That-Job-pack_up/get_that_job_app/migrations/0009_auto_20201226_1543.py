# Generated by Django 2.2.4 on 2020-12-26 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('get_that_job_app', '0008_auto_20201226_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='role', to='get_that_job_app.Role'),
        ),
    ]
