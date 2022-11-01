# Generated by Django 3.2.7 on 2022-11-01 07:40

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=50, verbose_name='タイトル')),
                ('comment', models.CharField(max_length=100, null=True, verbose_name='コメント')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='日付')),
                ('image1', models.CharField(max_length=256, null=True, verbose_name='画像1')),
                ('image2', models.CharField(max_length=256, null=True, verbose_name='画像2')),
                ('image3', models.CharField(max_length=256, null=True, verbose_name='画像3')),
                ('image4', models.CharField(max_length=256, null=True, verbose_name='画像4')),
                ('image5', models.CharField(max_length=256, null=True, verbose_name='画像5')),
            ],
            options={
                'db_table': 'diary_info',
            },
        ),
        migrations.CreateModel(
            name='Talkchat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名前')),
                ('sex', models.CharField(max_length=1, verbose_name='性別')),
                ('user_id', models.CharField(max_length=8, verbose_name='ユーザID')),
                ('user_type', models.CharField(max_length=1, verbose_name='ユーザタイプ')),
                ('image', models.CharField(max_length=256, null=True, verbose_name='画像')),
            ],
            options={
                'db_table': 'tc_info',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('no', models.CharField(max_length=11, primary_key=True, serialize=False, verbose_name='主キー')),
                ('name', models.CharField(max_length=20, verbose_name='名前')),
                ('datebirth', models.DateTimeField(null=True, verbose_name='生年月日')),
                ('sex', models.CharField(max_length=1, verbose_name='性別')),
                ('user_id', models.CharField(max_length=8, verbose_name='ユーザID')),
                ('user_pass', models.CharField(max_length=10, verbose_name='ユーザパスワード')),
                ('telnum', models.CharField(max_length=12, verbose_name='電話番号')),
                ('precycle', models.IntegerField(validators=[django.core.validators.MinValueValidator(8), django.core.validators.MaxValueValidator(8)], verbose_name='妊娠周期')),
                ('bloodtype', models.CharField(max_length=2, null=True, verbose_name='血液型')),
                ('symptoms', models.CharField(max_length=100, null=True, verbose_name='症状')),
                ('user_type', models.CharField(max_length=1, verbose_name='ユーザタイプ')),
                ('hospitalname', models.CharField(max_length=50, null=True, verbose_name='病院名')),
                ('image1', models.CharField(max_length=256, null=True, verbose_name='画像1')),
                ('image2', models.CharField(max_length=256, null=True, verbose_name='画像2')),
                ('image3', models.CharField(max_length=256, null=True, verbose_name='画像3')),
                ('image4', models.CharField(max_length=256, null=True, verbose_name='画像4')),
                ('image5', models.CharField(max_length=256, null=True, verbose_name='画像5')),
                ('last_login', models.DateTimeField(max_length=8, verbose_name='最終ログイン')),
            ],
            options={
                'db_table': 'User_info',
            },
        ),
    ]
