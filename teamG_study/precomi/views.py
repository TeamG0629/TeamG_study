from django.shortcuts import render
from django.views import generic
from .forms import UserCreateForm, DiaryCreateForm
from  django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import User, Diary
from django.contrib import messages
from django.urls import reverse_lazy



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

#diaryアップデート
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

#class PrecomiListView(LoginRequiredMixin, generic.ListView):
#    model = Precomi
#   template_name = 'precomi_list.html'
# #======================================================


