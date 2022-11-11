from django.urls import path
from .import views

app_name = 'precomi'
urlpatterns = [
    path('',views.IndexView.as_view(),name="index"),
    path('talk/',views.TalkView.as_view(),name="talk"),
    path('profile/',views.ProfileView.as_view(),name="profile"),
    path('profile_update/',views.ProfileUpdateView.as_view(),name="profile_update"),
    path('profile_create/',views.ProfileCreateView.as_view(),name="profile_create"),
    path('notice/',views.NoticeView.as_view(),name="notice"),
]