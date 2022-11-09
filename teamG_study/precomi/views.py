from django.shortcuts import render
from django.views import generic
from .forms import UserCreateForm
from  django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import User
from django.contrib import messages
from django.urls import reverse_lazy

from .forms import DiaryCreateForm
from .models import Diary

#index.htmlに飛ばす
class IndexView(generic.TemplateView):
    template_name = "index.html"

#talk.htmlに飛ばす
class TalkView(generic.TemplateView):
    template_name = "talk.html"

#profile.htmlに飛ばす
class ProfileView(generic.TemplateView):
    template_name = "profile.html"

#profile_update.htmlに飛ばす
class ProfileUpdateView(generic.TemplateView):
    template_name = "profile_update.html"

#緊急通知の画面に飛ばす
class NoticeView(generic.TemplateView):
    template_name = "notice.html"

#profile_create.htmlに飛ばす(新規作成)
class ProfileCreateView(LoginRequiredMixin, generic.CreateView):
    model = User
    template_name = 'profile_create.html'
    form_class = UserCreateForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.user = self.request.user
        user.save()
        messages.success(self.request, '作成しました')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "作成に失敗しました")
        return super().form_invalid(form)




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
class DiaryView(generic.TemplateView):
    model = Diary
    template_name = "diary.html"
#
#     def get_queryset(self):
#         diaries = Diary.objects.filter(user=self.request.user).order_by('-created_at')
#         return diaries

#diary詳細
class DiaryDetailView(LoginRequiredMixin, generic.DetailView):
    model = Diary
    template_name = 'diary_detail.html'


#diary作成
class DiaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Diary
    template_name = "diary_create.html"
    form_class = DiaryCreateForm
    success_url = reverse_lazy('precomi:diary')

    def form_valid(self, form):
        diary = form.save(commit=False)
        diary.user = self.request.user
        diary.save()
        messages.success(self.request, '日記を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '日記の作成に失敗しました。')
        return super().form_invalid(form)

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


