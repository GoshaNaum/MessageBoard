from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Announcement)
admin.site.register(Comment)
admin.site.register(AnnouncementCategory)
admin.site.register(Author)


