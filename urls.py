from django.conf.urls.defaults import patterns, include, url
#from blog.views import index

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('blog.views',
    # Examples:
    # url(r'^$', 'csvt01.views.home', name='home'),
    # url(r'^csvt01/', include('csvt01.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^blog/index/$','blog.views.index'),
    # url(r'^blog/index/$',index),
    # url(r'^blog/index/$','index'),
    # url(r'^blog/index/(?P<id>\d{2})/$','index'),  
    url(r'^blog/index/(\d{2})/$','index'),  
)	
