from django.shortcuts import render
from django.views import generic
from .forms import UserCreateForm
from django.urls import reverse_lazy
from  django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import User
from django.contrib import messages

#index.htmlに飛ばす
class IndexView(generic.TemplateView):
    template_name = "index.html"

#talk.htmlに飛ばす
class TalkView(generic.TemplateView):
    template_name = "talk.html"

#profile.htmlに飛ばす
class ProfileView(generic.ListView):
    template_name = "profile.html"
    def get_queryset(self):
        precomi = User.objects.all()
        return precomi

#profile_update.htmlに飛ばす
class ProfileUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = User
    template_name = "profile_update.html"
    form_class = UserUpdateForm
    

#緊急通知の画面に飛ばす
class NoticeView(generic.TemplateView):
    template_name = "notice.html"

#profile_create.htmlに飛ばす(新規作成)
class ProfileCreateView(LoginRequiredMixin, generic.CreateView):
    model = User
    template_name = 'profile_create.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('precomi:profile_create')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.user = self.request.user
        user.save()
        messages.success(self.request, '作成しました')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "作成に失敗しました")
        return super().form_invalid(form)