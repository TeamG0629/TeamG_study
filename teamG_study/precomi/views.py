from django.shortcuts import render
from django.views import generic
import win32com.client
import datetime
import schedule
import time

#index.htmlに飛ばす
class IndexView(generic.TemplateView):
    template_name = "index.html"


#talk.htmlに飛ばす
class TalkView(generic.TemplateView):
    template_name = "talk.html"

#notice.htmlに飛ばす
# class NoticeView(generic.TemplateView):
#     template_name = 'notice.html'

class NoticeView():
    # outlookを開く
    outlook = win32com.client.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)
    # ykh2135と@stu.o-hara.ac.jpの入力を省く。送り先
    mail.to = 'ykh2135238@stu.o-hara.ac.jp'
    mail.cc = ''
    mail.bcc = ''
    mail.subject = 'pythonプログラムから'
    mail.bodyFormat = 1
    mail.body = '''お疲れ様です。tsetです。

      testです。メッセージはきましたか？
      '''

    # 確認画面
    # mail.display(True)
    # 自動送信
    mail.Send()

    # schedule.every().day.at("14:15").do(job)


    schedule.every(10).seconds.do(job)

    while True:
        schedule.run_pending()
        time.sleep(60)


# #プロフィール===============================================
# #profile.htmlに飛ばす
# class ProfileView(generic.TemplateView):
#     template_name = "profile.html"
#
#
# #profile作成
# class ProfileCreateView(generic.CreateView):
#     model = User_info
#     template_name = "profile_create.html"
#
#
# #profileアップデート
# class ProfileUpdateView(generic.UpdateView):
#     model = User_info
#     template_name = "profile_update.html"
# #======================================================
#
#
# #日記===================================================
# #diary.htmlに飛ばす
# class DiaryView(generic.TemplateView):
#     template_name = "diary.html"
#
#
# #diary作成
# class DiaryCreateView(generic.CreateView):
#     model = Diary
#     template_name = "diary_create.html"
#
#
# #diaryアップデート
# class DiaryUpdateView(generic.UpdateView):
#     model = Diary
#     template_name = "diary_update.html"
#
#
# #diary削除
# class DiaryDeleteView(generic.DeleteView):
#     model = Diary
#     template_name = "diary_delete.html"
# #======================================================


