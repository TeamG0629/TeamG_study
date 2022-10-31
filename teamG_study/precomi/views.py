from django.shortcuts import render
from django.views import generic


#index.htmlに飛ばす
class IndexView(generic.TemplateView):
    template_name = "index.html"


#talk.htmlに飛ばす
class TalkView(generic.TemplateView):
    template_name = "talk.html"

#notice.htmlに飛ばす
class NoticeView(generic.TemplateView):
    template_name = 'notice.html'


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


