import os
from django import forms
from .models import User


#ユーザプロフィールの新規作成(名前、誕生日、性別、電話番号、妊娠周期、血液型、症状)
class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name','datebirth','sex','telnum','precycle','bloodtype','symptoms')
    def __int__(self,args,**kwargs):
        super().__init__(*args,**kwargs)
        for fields in self.fields.values():
            fields.widget.attrs['class'] = 'form-control'