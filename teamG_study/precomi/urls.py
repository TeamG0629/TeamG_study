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
    path('diary/',views.DiaryView.as_view(),name="diary"),
    path('diary-detail/<int:pk>/', views.DiaryDetailView.as_view(), name="diary_detail"),
    path('diary-create',views.DiaryCreateView.as_view(),name="diary_create"),
    path('diary-update/<int:pk>/',views.DiaryUpdateView.as_view(),name="diary_update"),
    path('diary-delete/<int:pk>/',views.DiaryDeleteView.as_view(),name="diary_delete"),
    path('inquiry/',views.InquiryView.as_view(),name="inquiry"),
    path('profile/',views.ProfileView.as_view(),name="profile"),

]