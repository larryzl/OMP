# Generated by Django 3.1.4 on 2021-10-20 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('db_models', '0014_upload_package_history_package_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='InspectionHistory',
            fields=[
                ('id', models.AutoField(help_text='自增主键', primary_key=True, serialize=False, unique=True)),
                ('inspection_name', models.CharField(help_text='报告名称:巡检类型名称', max_length=256)),
                ('inspection_type', models.CharField(default='service', help_text='巡检类型，service、host、deep', max_length=32)),
                ('inspection_status', models.IntegerField(default=0, help_text='巡检状态: 0-未开始；1-进行中；2-成功；3-失败')),
                ('execute_type', models.CharField(default='man', help_text='执行方式: 手动-man；定时：auto', max_length=32)),
                ('inspection_operator', models.CharField(help_text='操作人员-当前登录人', max_length=16)),
                ('hosts', models.JSONField(blank=True, help_text="巡检主机:[{'id':'1', 'ip':'10.0.9.158'}]", null=True)),
                ('services', models.JSONField(blank=True, help_text='巡检组件', null=True)),
                ('start_time', models.DateTimeField(auto_now_add=True, help_text='开始时间')),
                ('end_time', models.DateTimeField(help_text='结束时间，后端后补', null=True)),
                ('duration', models.IntegerField(default=0, help_text='巡检用时：单位s，后端后补')),
                ('env', models.ForeignKey(help_text='当前环境id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='db_models.env', verbose_name='当前环境id')),
            ],
            options={
                'verbose_name': '巡检记录历史表',
                'verbose_name_plural': '巡检记录历史表',
                'db_table': 'inspection_history',
                'ordering': ('-start_time',),
            },
        ),
        migrations.CreateModel(
            name='InspectionReport',
            fields=[
                ('id', models.AutoField(help_text='自增主键', primary_key=True, serialize=False, unique=True)),
                ('tag_total_num', models.IntegerField(default=0, help_text='总指标数')),
                ('tag_error_num', models.IntegerField(default=0, help_text='异常指标数')),
                ('risk_data', models.JSONField(blank=True, help_text='风险指标', null=True)),
                ('host_data', models.JSONField(blank=True, help_text='主机列表', null=True)),
                ('serv_plan', models.JSONField(blank=True, help_text='服务平面图', null=True)),
                ('serv_data', models.JSONField(blank=True, help_text='服务列表', null=True)),
                ('inst_id', models.OneToOneField(help_text='巡检记录历史表id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='inspection.inspectionhistory', verbose_name='巡检记录历史表')),
            ],
            options={
                'verbose_name': '巡检任务 报告数据',
                'verbose_name_plural': '巡检任务 报告数据',
                'db_table': 'inspection_report',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='InspectionCrontab',
            fields=[
                ('id', models.AutoField(help_text='自增主键', primary_key=True, serialize=False, unique=True)),
                ('job_type', models.IntegerField(choices=[(0, '深度分析'), (1, '主机巡检'), (2, '组件巡检')], default=0, help_text='任务类型：0-深度分析 1-主机巡检 2-组建巡检')),
                ('job_name', models.CharField(help_text='任务名称', max_length=128)),
                ('is_start_crontab', models.IntegerField(default=0, help_text='是否开启定时任务：0-开启，1-关闭')),
                ('crontab_detail', models.JSONField(help_text='定时任务详情')),
                ('create_date', models.DateTimeField(auto_now_add=True, help_text='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='修改时间')),
                ('env', models.ForeignKey(help_text='环境', null=True, on_delete=django.db.models.deletion.SET_NULL, to='db_models.env', verbose_name='环境')),
            ],
            options={
                'verbose_name': '巡检任务 定时配置表',
                'verbose_name_plural': '巡检任务 定时配置表',
                'db_table': 'inspection_crontab',
                'ordering': ('id',),
            },
        ),
    ]
