from django.urls import path
from .views import AnnouncementsList, AnnouncementDetail, CategoryListView, SearchAnnouncementsList, \
AnnouncementCreate, AnnouncementUpdate, AnnouncementDelete
urlpatterns = [
    path('announcements/', AnnouncementsList.as_view(), name='announcements'),
    path('announcements/<int:pk>', AnnouncementDetail.as_view(), name='announcement'),
    path('announcements/search/', SearchAnnouncementsList.as_view(), name='search'),
    path('announcement/create/', AnnouncementCreate.as_view(), name='announcement_create'),
    path('announcement/<int:pk>/edit', AnnouncementUpdate.as_view(), name='announcement_edit'),
    path('announcements/<int:pk>/delete', AnnouncementDelete.as_view(), name='announcement_delete'),
    path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
]

