from django.conf.urls import url
from django.conf.urls.static import static

from mysite import settings
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^problem/(?P<pk>\d+)/$', views.problem_detail, name='problem_detail'),
    url(r'^problem/new/$', views.problem_new, name='problem_new'),
    url(r'^problem/(?P<pk>\d+)/edit/$', views.problem_edit, name='problem_edit'),
    url(r'^drafts/$', views.problem_draft_list, name='problem_draft_list'),
    url(r'^problem/(?P<pk>\d+)/publish/$', views.problem_publish, name='problem_publish'),
    url(r'^problem/(?P<pk>\d+)/remove/$', views.problem_remove, name='problem_remove'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

