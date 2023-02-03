from django.db import models
from django.utils import timezone
from accounts.models import CustomUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.validators import RegexValidator

import uuid

#プロフィールモデル
#(主キー、名前、生年月日、性別、ユーザパスワード、電話番号、妊娠周期、血液型、症状、ユーザタイプ、病院名、画像5枚、最終ログイン,コメント,緊急連絡先)
class User(models.Model):
    blood = (
        ("A","A型"),
        ("B","B型"),
        ("AB","AB型"),
        ("O","O型")
    )
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    no = models.AutoField(verbose_name='主キー',primary_key=True)
    name = models.CharField(max_length=20,verbose_name='名前',null=False)
    datebirth = models.DateField(verbose_name='生年月日',null=True)
    user_pass = models.CharField(max_length=10,verbose_name='ユーザパスワード',null=False)
    tel_number_regex = RegexValidator(regex=r'^[0-9]+$', message=("半角数字のみを入力してください"))
    telnum = models.CharField(validators=[tel_number_regex], max_length=12, verbose_name='電話番号', null=False)
    precycle = models.IntegerField(validators=[MinValueValidator(8)],verbose_name='妊娠周期',null=False)
    bloodtype = models.CharField(max_length=2,verbose_name='血液型', choices=blood, null=True)
    symptoms = models.CharField(max_length=100,verbose_name='症状',null=True)
    user_type = models.CharField(max_length=1,verbose_name='ユーザタイプ',null=False)
    hospitalname = models.CharField(max_length=50,verbose_name='病院名',null=True)
    image1 = models.ImageField(verbose_name='画像1',null=True)
    image2 = models.ImageField(verbose_name='画像2',null=True)
    image3 = models.ImageField(verbose_name='画像3',null=True)
    image4 = models.ImageField(verbose_name='画像4',null=True)
    image5 = models.ImageField(verbose_name='画像5',null=True)
    last_login = models.DateTimeField(max_length=8,verbose_name='最終ログイン',auto_now=True)
    comment = models.TextField(verbose_name='コメント',null=True)
    egcontact = models.EmailField(verbose_name='緊急連絡先',null=True)

    class Meta:
        db_table = 'User_info'

    #user_idがレコードで識別する文字列
    def __str__(self):
        return self.user



#日記モデル(画像5枚、タイトル、コメント、日付、公開非公開設定、公開用ネーム設定)
class Diary(models.Model):
    IS_USED_CHOICES = (
        (True,'公開'),
        (False, '非公開'),
    )
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    title = models.CharField(max_length=50,verbose_name='タイトル',null=False)
    comment = models.TextField(verbose_name='コメント',null=True)
    date = models.DateField(default=timezone.now,verbose_name='日付')
    image1 = models.ImageField(verbose_name='画像1', blank=True, null=True)
    image2 = models.ImageField(verbose_name='画像2', blank=True, null=True)
    image3 = models.ImageField(verbose_name='画像3', blank=True, null=True)
    image4 = models.ImageField(verbose_name='画像4', blank=True, null=True)
    image5 = models.ImageField(verbose_name='画像5', blank=True, null=True)
    publicprivate = models.BooleanField(verbose_name='公開非公開', choices=IS_USED_CHOICES,blank=True, null=True)
    publicname = models.CharField(verbose_name='公開用ネーム',max_length=50,blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    class Meta:
        db_table = 'diary_info'

    def __str__(self):
        return self.title

#トークチャットモデル(名前、性別、ユーザID、ユーザタイプ、画像1枚)
class Talkchat(models.Model):
    name = models.CharField(max_length=20,verbose_name='名前',null=False)
    user_id = models.CharField(max_length=8,verbose_name='ユーザID',null=False)
    user_type = models.CharField(max_length=1,verbose_name='ユーザタイプ',null=False)
    image = models.CharField(max_length=256,verbose_name='画像',null=True)
    class Meta:
        db_table = 'tc_info'

#コメントモデル


#日記コメント(名前、コメント、日時、対象コメント)
class DiaryComment(models.Model):
    name = models.CharField('名前',max_length=255,default='名無し')
    comment = models.TextField('本文')
    target = models.ForeignKey(Diary, on_delete=models.CASCADE, verbose_name='対象記事',null=True)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.comment[:20]


class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)

class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    room = models.ForeignKey(
        Room,
        blank=True,
        null=True,
        related_name='room_meesages',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)