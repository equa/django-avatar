try:
    from django.conf.urls import patterns, url
except ImportError:
    # Django < 1.4
    from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('avatar.views',
    url(r'^add/$', 'add', name='avatar_add'),
    url(r'^change/$', 'change', name='avatar_change'),
    url(r'^delete/$', 'delete', name='avatar_delete'),
    url(r'^render_primary/(?P<user_id>[\d]+)/(?P<size>[\d]+)/$', 'render_primary', name='avatar_render_primary'),
#    url(r'^list/(?P<user_id>[\d]+)/$', 'avatar_gallery', name='avatar_gallery'),
#    url(r'^list/(?P<user_id>[\d]+)/(?P<id>[\d]+)/$', 'avatar', name='avatar'),
)
