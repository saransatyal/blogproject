from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from blog import views as uploader_view
from blog import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from accounts import views as accounts_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.temp , name='temp'),
    url(r'^readarticle/(?P<pk>\d+)/$', views.readarticle, name='readarticle'),
    url(r'^home1$', views.home1 , name='home1'),
    url(r'^base/$', views.base , name='base'),
    url(r'^simple_upload/$', uploader_view.simple_upload , name='simple_upload'),
    url(r'^signup/$', accounts_views.signup , name = "signup" )
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
