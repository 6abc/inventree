from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('', include('app1.urls')),
    path('', include('accounts.urls')),
    path('admin/', admin.site.urls),
]

# ✅ Explicit media serving (works with DEBUG=False + Gunicorn)
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]
