from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("main.urls")),
    path("wallet/", include("wallet.urls")),
    path("app/", include("app_user.urls")),

]

handler404 = 'app_user.views.error_404'
handler500 = 'app_user.views.error_500'
handler404 = 'main.views.error_404'
handler500 = 'main.views.error_500'
handler404 = 'wallet.views.error_404'
handler500 = 'wallet.views.error_500'


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)