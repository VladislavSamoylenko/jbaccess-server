import api_commons.common
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('web_ui.urls')),
    url(r'^api/?', include('jba_api.urls')),
    url(r'^admin/?', admin.site.urls),
]

handler404 = api_commons.common.error_404_handler
handler500 = api_commons.common.error_500_handler
