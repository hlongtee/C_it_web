# Generated by Django 2.2.4 on 2019-09-14 09:47

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bureau',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bureau_name', models.CharField(help_text='地市局名', max_length=10, verbose_name='地市局名')),
            ],
            options={
                'verbose_name': '地市局信息表',
                'verbose_name_plural': '地市局信息表',
                'db_table': 'tb_bureau',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_name', models.CharField(help_text='部门', max_length=20, verbose_name='部门')),
            ],
            options={
                'verbose_name': '部门信息表',
                'verbose_name_plural': '部门信息表',
                'db_table': 'tb_Dep',
            },
        ),
        migrations.CreateModel(
            name='ParentDepartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_name', models.CharField(help_text='上级部门', max_length=20, verbose_name='上级部门')),
                ('own_bureau', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='apps.user.Bureau')),
            ],
            options={
                'verbose_name': '地市局信息表',
                'verbose_name_plural': '地市局信息表',
                'db_table': 'tb_ParentDep',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('job', models.CharField(blank=True, help_text='职务', max_length=20, verbose_name='职务')),
                ('others', models.CharField(blank=True, help_text='备注', max_length=40, verbose_name='备注')),
                ('mobile', models.CharField(error_messages={'unique': '此手机号已经注册'}, help_text='手机号', max_length=11, verbose_name='手机号')),
                ('dep_name', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='apps.user.Department')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('parent_name', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='apps.user.ParentDepartment')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'tb_Users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
