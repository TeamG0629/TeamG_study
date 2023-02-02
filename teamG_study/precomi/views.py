from django.shortcuts import render,redirect,get_object_or_404
from django.views import generic
from .forms import UserCreateForm, DiaryCreateForm, InquiryForm ,CommentCreateForm
from  django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import User, Diary ,DiaryComment
from django.contrib import messages
from django.urls import reverse_lazy

#実験
from django.views.generic.edit import CreateView


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
    paginate_by = 4

    def get_queryset(self):
        diaries = Diary.objects.filter(user=self.request.user).order_by('-created_at')
        return diaries

#diary詳細
class DiaryDetailView(LoginRequiredMixin, generic.DetailView):
    model = Diary
    template_name = 'diary_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print((self.kwargs['pk']))
        context['comments'] = DiaryComment.objects.filter(target=Diary.objects.get(id=self.kwargs['pk']))
        return context

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

#全体表示日記htmlに飛ばす
class AlldiaryView(LoginRequiredMixin,generic.ListView):
    model = Diary
    template_name = "alldiary.html"
    paginate_by = 4


    def get_queryset(self):
        diaries = Diary.objects.all().exclude(user=self.request.user).filter(publicprivate=True).order_by('-created_at')

        return diaries

#コメント投稿ページのビュー
class CommentView(CreateView):
    template_name = 'comment_form.html'
    model = DiaryComment
    form_class = CommentCreateForm
    #success_url = '/'

    #フォームに入力された情報が正しい場合の処理
    def form_valid(self, form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(Diary,pk=post_pk)
        comment = form.save(commit=False)
        comment.target = post
        comment.save()
        print("ヴァリデーションOK")
        # print("ここまでやってる")
        # return redirect('/')
        return redirect('precomi:diary_detail',pk=post_pk)
    # diary-detail/2/
    def form_invalid(self, form):
        print("ヴァリデーションNG")
        return redirect('/')

    #htmlテンプレートに渡すデータを定義
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Diary,pk=self.kwargs['pk'])
        return context
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

def chat_index(request):
    return render(request, "chat_index.html")

def chat_room(request, room_name):
    return render(request, "chat_room.html", {"room_name": room_name})


