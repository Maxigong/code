from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,re_path, include


from .views import IndexTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('backend_work.urls')),


    # next path should be at the end
    # re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point"),
    re_path(r"^(?!media).*$", IndexTemplateView.as_view(), name="entry-point")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
