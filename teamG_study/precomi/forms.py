import os
from django import forms
from .models import User
from .models import Diary


#ユーザプロフィールの新規作成(誕生日、性別、電話番号、妊娠周期、血液型、症状)
class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('datebirth','sex','telnum','precycle','bloodtype','symptoms')
    def __int__(self,args,**kwargs):
        super().__init__(*args,**kwargs)
        for fields in self.fields.values():
            fields.widget.attrs['class'] = 'form-control'

class DiaryCreateForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ('title', 'comment', 'image1', 'image2', 'image3', 'image4', 'image5',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'