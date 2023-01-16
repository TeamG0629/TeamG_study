# Generated by Django 3.2.7 on 2022-12-01 01:10

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
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
                ('no', models.AutoField(primary_key=True, serialize=False, verbose_name='主キー')),
                ('name', models.CharField(max_length=20, verbose_name='名前')),
                ('datebirth', models.DateField(null=True, verbose_name='生年月日')),
                ('sex', models.CharField(max_length=1, verbose_name='性別')),
                ('user_pass', models.CharField(max_length=10, verbose_name='ユーザパスワード')),
                ('telnum', models.CharField(max_length=12, verbose_name='電話番号')),
                ('precycle', models.IntegerField(validators=[django.core.validators.MinValueValidator(8)], verbose_name='妊娠周期')),
                ('bloodtype', models.CharField(max_length=2, null=True, verbose_name='血液型')),
                ('symptoms', models.CharField(max_length=100, null=True, verbose_name='症状')),
                ('user_type', models.CharField(max_length=1, verbose_name='ユーザタイプ')),
                ('hospitalname', models.CharField(max_length=50, null=True, verbose_name='病院名')),
                ('image1', models.ImageField(null=True, upload_to='', verbose_name='画像1')),
                ('image2', models.ImageField(null=True, upload_to='', verbose_name='画像2')),
                ('image3', models.ImageField(null=True, upload_to='', verbose_name='画像3')),
                ('image4', models.ImageField(null=True, upload_to='', verbose_name='画像4')),
                ('image5', models.ImageField(null=True, upload_to='', verbose_name='画像5')),
                ('last_login', models.DateTimeField(auto_now=True, max_length=8, verbose_name='最終ログイン')),
                ('comment', models.TextField(null=True, verbose_name='コメント')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
            options={
                'db_table': 'User_info',
            },
        ),
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='タイトル')),
                ('comment', models.TextField(max_length=100, null=True, verbose_name='コメント')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='日付')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像1')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像2')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像3')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像4')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像5')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
            options={
                'db_table': 'diary_info',
            },
        ),
    ]
