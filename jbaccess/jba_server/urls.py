import api_commons.common
from django.conf.urls import url, include
from django.conf.urls.static import static
from jba_server.settings import base as settings

urlpatterns = [
    url(r'^', include('jba_api.urls')),
    url(r'^admin/$', include('web_ui.urls'))
]

handler404 = api_commons.common.error_404_handler
handler500 = api_commons.common.error_500_handler
