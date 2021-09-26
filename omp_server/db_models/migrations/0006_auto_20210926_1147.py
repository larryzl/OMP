# Generated by Django 3.1.4 on 2021-09-26 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db_models', '0005_monitorurl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alert',
            name='env_id',
        ),
        migrations.AddField(
            model_name='alert',
            name='env',
            field=models.ForeignKey(help_text='环境', null=True, on_delete=django.db.models.deletion.SET_NULL, to='db_models.env', verbose_name='环境'),
        ),
        migrations.AlterField(
            model_name='operatelog',
            name='request_result',
            field=models.TextField(default='success', help_text='请求结果', verbose_name='请求结果'),
        ),
    ]
