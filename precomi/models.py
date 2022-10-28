from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator



#プロフィールモデル
#(主キー、名前、生年月日、性別、ユーザID、ユーザパスワード、電話番号、妊娠周期、血液型、症状、ユーザタイプ、病院名、画像5枚、最終ログイン)
class User(models.Model):
    no = models.CharField(max_length=11,primary_key=True)
    name = models.CharField(max_length=20,null=False)
    datebirth = models.DateTimeField(null=True)
    sex = models.CharField(max_length=1,null=False)
    user_id = models.CharField(max_length=8,null=False)
    user_pass = models.CharField(max_length=10,null=False)
    telnum = models.CharField(max_length=12,null=False)
    precycle = models.IntegerField(validators=[MinValueValidator(8),MaxValueValidator(8)],null=False)
    bloodtype = models.CharField(max_length=2,null=True)
    symptoms = models.CharField(max_length=100,null=True)
    user_type = models.CharField(max_length=1,null=False)
    hospitalname = models.CharField(max_length=50,null=True)
    image1 = models.CharField(max_length=256,null=True)
    image2 = models.CharField(max_length=256,null=True)
    image3 = models.CharField(max_length=256,null=True)
    image4 = models.CharField(max_length=256,null=True)
    image5 = models.CharField(max_length=256,null=True)
    last_login = models.DateTimeField(max_length=8,null=False)


    class Meta:
        db_table = 'User_info'

    #user_idがレコードで識別する文字列
    def __str__(self):
        return self.user_id


#日記モデル(画像5枚、タイトル、コメント、日付)
# class Diary(models.Model):
#     tittle = models.CharField(max_length=50,null=False)
#     comment = models.CharField(max_length=100,null=True)
#     date = models.DateField(default=timezone.now)
#     image1 = models.ForeignKey(User)
#     image2 = models.ForeignKey(User)
#     image3 = models.ForeignKey(User)
#     image4 = models.ForeignKey(User)
#     image5 = models.ForeignKey(User)
#     class Meta:
#         db_table = 'diary_info'
#
# #トークチャットモデル(名前、性別、ユーザID、ユーザタイプ、画像1枚)
# class Talkchat(models.Model):
#     name = models.ForeignKey(User)
#     sex = models.ForeignKey(User)
#     user_id = models.ForeignKey(User)
#     user_type = models.ForeignKey(User)
#     image = models.ForeignKey(User)
#     class Meta:
#         db_table = 'tc_info'