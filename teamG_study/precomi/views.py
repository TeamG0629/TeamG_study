from django.shortcuts import render
from django.views import generic
from .forms import UserCreateForm, DiaryCreateForm, InquiryForm
from  django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import User, Diary
from django.contrib import messages
from django.urls import reverse_lazy


import logging
logger = logging.getLogger(__name__)

#index.htmlに飛ばす
class IndexView(generic.TemplateView):
    template_name = "index.html"

#talk.htmlに飛ばす
class TalkView(generic.TemplateView):
    template_name = "talk.html"

#緊急通知の画面に飛ばす
class NoticeView(generic.TemplateView):
    template_name = "notice.html"


# #diary.htmlに飛ばす
class DiaryView(LoginRequiredMixin, generic.ListView):
    model = Diary
    template_name = "diary.html"
    paginate_by = 2

    def get_queryset(self):
        diaries = Diary.objects.filter(user=self.request.user).order_by('-created_at')
        return diaries

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
        messages.error(self.request, "日記の作成に失敗しました。")
        return super().form_invalid(form)

#diary更新
class DiaryUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Diary
    template_name = "diary_update.html"
    form_class = DiaryCreateForm

    def get_success_url(self):
        return reverse_lazy('precomi:diary_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '日記を更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "日記の更新に失敗しました。")
        return super().form_invalid(form)

# #diary削除
class DiaryDeleteView(generic.DeleteView):
    model = Diary
    template_name = "diary_delete.html"
    success_url = reverse_lazy('precomi:diary')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "日記を削除しました。")
        return super().delete(request, *args, **kwargs)


# #======================================================

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('precomi:inquiry')

    def form_valid(self,form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)


#profile.htmlに飛ばす
class ProfileView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = "profile.html"

    def get_queryset(self):
        profile = User.objects.filter(user=self.request.user)
        return profile


class ProfileCreateView(LoginRequiredMixin, generic.CreateView):
    model = User
    template_name = 'profile_create.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('precomi:profile')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.user = self.request.user
        user.save()
        messages.success(self.request, '作成しました')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "作成に失敗しました")
        return super().form_invalid(form)

#profile_update.htmlに飛ばす
class ProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = User
    template_name = "profile_update.html"
    form_class = UserCreateForm

    def get_success_url(self):
        return reverse_lazy('precomi:profile')

    def form_valid(self, form):
        messages.success(self.request, 'プロフィールを更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "プロフィールの更新に失敗しました。")
        return super().form_invalid(form)


