from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from userprofiles.views import sign_up, sign_in, sign_out

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comments/', include("comments.urls", namespace='comments')),
    path('', include('rest.urls')),
	path('', include("userprofiles.urls", namespace='userprofiles')),
    path('', include("post.urls", namespace='posts')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
