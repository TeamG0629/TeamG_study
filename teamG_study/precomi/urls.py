from django.urls import path
from .import views

app_name = 'precomi'
urlpatterns = [
    path('',views.IndexView.as_view(),name="index"),
    path('notice/',views.NoticeView.as_view(),name="notice"),
    # path('profile/',views.ProfileView(),name="profile"),
    # path('profile-create',views.ProfileCreateView(),name="profile_create"),
    # path('profile-update',views.ProfileUpdateView(),name="profile_update"),
    # path('diary/',views.DiaryView(),name="diary"),
    # path('diary-create',views.DiaryCreateView(),name="diary_create"),
    # path('diary-update',views.DiaryUpdateView(),name="diary_update"),
    # path('diary-delete',views.DiaryDeleteView(),name="diary_delete"),
]