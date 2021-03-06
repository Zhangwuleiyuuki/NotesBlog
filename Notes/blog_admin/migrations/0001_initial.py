# Generated by Django 2.2.12 on 2021-01-06 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=16, unique=True)),
                ('password', models.CharField(max_length=64)),
                ('user_permissions', models.CharField(max_length=4)),
                ('user_email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': '博客管理员',
                'verbose_name_plural': '博客管理员',
                'ordering': ['id'],
            },
        ),
    ]
