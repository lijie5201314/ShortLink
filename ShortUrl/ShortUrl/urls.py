from django.conf.urls import url
from django.contrib import admin
from short_url import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^longtoshort$',views.longtoshort,name='longtoshort'),
    url(r'^shortcustom$',views.shortcustom,name='shortcustom'),
    url(r'^([0-9a-zA-Z]+)$',views.shorttolong,name='shorttolong'),
]
