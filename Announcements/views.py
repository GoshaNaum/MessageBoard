from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Announcement, Comment, Category
from .filters import AnnouncementFilter
from .forms import AnnouncementForm
from datetime import datetime
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect, get_object_or_404, render


class AnnouncementsList(ListView):
    model = Announcement
    template_name = 'announcements.html'
    context_object_name = 'announcements'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


class AnnouncementDetail(DetailView):
    model = Announcement
    template_name = 'announcement.html'
    context_object_name = 'announcement'

    def get_context_data(self, **kwargs):
        context = super(AnnouncementDetail, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(announcement__id=self.kwargs['pk'])
        return context


class CategoryListView(ListView):
    model = Announcement
    template_name = 'category_list.html'
    context_object_name = 'category_announcement_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Announcement.objects.filter(category=self.category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        return context


class SearchAnnouncementsList(ListView):
    model = Announcement
    template_name = 'search.html'
    context_object_name = 'search_announcements'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = AnnouncementFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class AnnouncementCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('announcements.add_post')
    form_class = AnnouncementForm
    model = Announcement
    template_name = 'announcement_create.html'


class AnnouncementUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('announcements.change_post')
    form_class = AnnouncementForm
    model = Announcement
    template_name = 'announcement_create.html'


class AnnouncementDelete(DeleteView):
    model = Announcement
    template_name = 'announcement_delete.html'
    success_url = reverse_lazy('announcements')


