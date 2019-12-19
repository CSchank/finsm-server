from django.conf.urls import url
from finsm_frontend import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #url(r'^$', views.FinsmAppView.as_view(), name='home'), # Notice the URL has been named
    #url(r'finsm.min.js', views.FinsmJSView.as_view(), name='home'), # Notice the URL has been named
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)