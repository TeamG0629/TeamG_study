import os
from django import forms
from .models import User, Diary, DiaryComment
from django.core.mail import EmailMessage

#ユーザプロフィールの新規作成(誕生日、性別、電話番号、妊娠周期、血液型、コメント、緊急連絡先)
class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'datebirth','telnum','precycle','bloodtype','comment', 'image1','egcontact')
        widgets = {
            'datebirth': forms.SelectDateWidget(years=[x for x in range(1980, 2022)])
        }
        MONTHS = {
            1: 'jan', 2: 'feb', 3: 'mar', 4: 'apr',
            5: 'may', 6: 'jun', 7: 'jul', 8: 'aug',
            9: 'sep', 10: 'oct', 11: 'nov', 12: 'dec'
        }
        forms.SelectDateWidget(months=MONTHS)

    def __int__(self,args,**kwargs):
        super().__init__(*args,**kwargs)
        for fields in self.fields.values():
            fields.widget.attrs['class'] = 'form-control'


class InquiryForm(forms.Form):
    name = forms.CharField(label='お名前', max_length=30)
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='タイトル', max_length=30)
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control col-9'
        self.fields['name'].widget.attrs['placeholder'] = 'お名前をここに入力してください。'

        self.fields['email'].widget.attrs['class'] = 'form-control col-11'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスをここに入力してください。'

        self.fields['title'].widget.attrs['class'] = 'form-control col-11'
        self.fields['title'].widget.attrs['placeholder'] = 'タイトルをここに入力してください。'

        self.fields['message'].widget.attrs['class'] = 'form-control col-12'
        self.fields['message'].widget.attrs['placeholder'] = 'メッセージをここに入力してください。'

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']

        subject = 'お問い合わせ {}'.format(title)
        message = '送信者名: {0}\nメールアドレス: {1}\nメッセージ:\n{2}'.format(name, email, message)
        from_email = 'teamgtnkma@outlook.jp'
        to_list = [
            'teamgtnkma@outlook.jp'
        ]
        cc_list = [
            email

        ]

        message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list, cc=cc_list)
        message.send()

class DiaryCreateForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ('title', 'comment', 'image1', 'image2', 'image3', 'image4', 'image5','publicprivate','publicname')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'




#コメント投稿フォーム
class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = DiaryComment
        exclude = ('target', 'created_at')