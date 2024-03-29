from django.urls import path
from .import views
app_name = 'precomi'
urlpatterns = [
    path('',views.IndexView.as_view(),name="index"),
    path('talk/',views.TalkView.as_view(),name="talk"),
    path('notice/',views.NoticeView.as_view(),name="notice"),
    path('diary/',views.DiaryView.as_view(),name="diary"),
    path('diary-detail/<int:pk>/', views.DiaryDetailView.as_view(), name="diary_detail"),
    path('diary-create',views.DiaryCreateView.as_view(),name="diary_create"),
    path('diary-update/<int:pk>/',views.DiaryUpdateView.as_view(),name="diary_update"),
    path('diary-delete/<int:pk>/',views.DiaryDeleteView.as_view(),name="diary_delete"),
    path('inquiry/',views.InquiryView.as_view(),name="inquiry"),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('profile_update/<int:pk>/', views.ProfileUpdateView.as_view(), name="profile_update"),
    path('profile_create/', views.ProfileCreateView.as_view(), name="profile_create"),
    path('alldiary/',views.AlldiaryView.as_view(),name="alldiary"),
    path('comment/create/<int:pk>',views.CommentView.as_view(),name='comment_create'),

    # path("chat/", views.chat_index, name="chat_index"),
    path('chat/', views.ChatIndexView.as_view(), name='chat_index'),
    path("chat_r/<str:room_name>/", views.chat_room, name="chat_room"),
    path('room/', views.room, name='room'),

]