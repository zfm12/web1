from django.contrib import admin
from django.conf.urls import include,url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('admin/', admin.site.urls),
	url(r'^admin/',admin.site.urls),               #django发生了变化
	url(r'',include(('syy_topics.urls','syy_topics'),namespace='syy_topics')),
	url(r'^users/',include(('users.urls','users'),namespace='users')),
	url(r'',include(('syy_contacts.urls','syy_contacts'),namespace='syy_contacts')),
	#url(r'^static/(?P<path>.*)$', static.server, {'document_root': settings.STATIC_ROOT}, name='static')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)