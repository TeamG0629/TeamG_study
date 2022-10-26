from django.db import models



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
    precycle = models.IntegerField(max_length=8,null=False)
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


#日記モデル
class Diary(models.Model):


#トークチャットモデル
class Talkchat(models.Model):
    