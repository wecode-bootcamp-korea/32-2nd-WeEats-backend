# Generated by Django 4.0.4 on 2022-05-18 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('kakao_id', models.BigIntegerField()),
                ('name', models.CharField(max_length=100)),
                ('profile_image', models.CharField(max_length=1000)),
                ('email', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
