from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator



#プロフィールモデル
#(主キー、名前、生年月日、性別、ユーザID、ユーザパスワード、電話番号、妊娠周期、血液型、症状、ユーザタイプ、病院名、画像5枚、最終ログイン)
class User(models.Model):
    no = models.CharField(max_length=11,verbose_name='主キー',primary_key=True)
    name = models.CharField(max_length=20,verbose_name='名前',null=False)
    datebirth = models.DateTimeField(verbose_name='生年月日',null=True)
    sex = models.CharField(max_length=1,verbose_name='性別',null=False)
    user_id = models.CharField(max_length=8,verbose_name='ユーザID',null=False)
    user_pass = models.CharField(max_length=10,verbose_name='ユーザパスワード',null=False)
    telnum = models.CharField(max_length=12,verbose_name='電話番号',null=False)
    precycle = models.IntegerField(validators=[MinValueValidator(8),MaxValueValidator(8)],verbose_name='妊娠周期',null=False)
    bloodtype = models.CharField(max_length=2,verbose_name='血液型',null=True)
    symptoms = models.CharField(max_length=100,verbose_name='症状',null=True)
    user_type = models.CharField(max_length=1,verbose_name='ユーザタイプ',null=False)
    hospitalname = models.CharField(max_length=50,verbose_name='病院名',null=True)
    image1 = models.CharField(max_length=256,verbose_name='画像1',null=True)
    image2 = models.CharField(max_length=256,verbose_name='画像2',null=True)
    image3 = models.CharField(max_length=256,verbose_name='画像3',null=True)
    image4 = models.CharField(max_length=256,verbose_name='画像4',null=True)
    image5 = models.CharField(max_length=256,verbose_name='画像5',null=True)
    last_login = models.DateTimeField(max_length=8,verbose_name='最終ログイン',null=False)


    class Meta:
        db_table = 'User_info'

    #user_idがレコードで識別する文字列
    def __str__(self):
        return self.user_id


#日記モデル(画像5枚、タイトル、コメント、日付)
class Diary(models.Model):
    tittle = models.CharField(max_length=50,verbose_name='タイトル',null=False)
    comment = models.CharField(max_length=100,verbose_name='コメント',null=True)
    date = models.DateField(default=timezone.now,verbose_name='日付')
    image1 = models.CharField(max_length=256,verbose_name='画像1',null=True)
    image2 = models.CharField(max_length=256,verbose_name='画像2',null=True)
    image3 = models.CharField(max_length=256,verbose_name='画像3',null=True)
    image4 = models.CharField(max_length=256,verbose_name='画像4',null=True)
    image5 = models.CharField(max_length=256,verbose_name='画像5',null=True)
    class Meta:
        db_table = 'diary_info'

#トークチャットモデル(名前、性別、ユーザID、ユーザタイプ、画像1枚)
class Talkchat(models.Model):
    name = models.CharField(max_length=20,verbose_name='名前',null=False)
    sex = models.CharField(max_length=1,verbose_name='性別',null=False)
    user_id = models.CharField(max_length=8,verbose_name='ユーザID',null=False)
    user_type = models.CharField(max_length=1,verbose_name='ユーザタイプ',null=False)
    image = models.CharField(max_length=256,verbose_name='画像',null=True)
    class Meta:
        db_table = 'tc_info'

