from django.conf.urls import url,include

from . import views
from .dependentpages import footerpages



app_name="webPage"#namespacing url names   used in tempalte url()
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog$', views.blog, name='blog'),
    url(r'^blog/year/(?P<year>[0-9]{4})/$', views.blog_year_archive, name='blog_year_archive'),
    url(r'^blog/category/(?P<category_id>[0-9]+)/$', views.blog_category_archive, name='blog_category_archive'),
    url(r'^blog/detail/(?P<name>[^/]+)/$', views.blog_detail, name='blog_detail'),
    url(r'^portfolio$', views.portfolio, name='portfolio'),
    url(r'^portfolio/detail/(?P<name>[^/]+)/$', views.portfolio_detail, name='portfolio_detail'),
    url(r'^archive$', views.archive, name='archive'),
    url(r'^colleciton$', views.collection, name='collection'),
    url(r'^cheetSheet$', views.cheetSheet, name='cheetSheet'),
    url(r'^about$', views.about, name='about'),


    url(r'^caicai$', views.theone, name='theone'),

    url(r'^contact$',footerpages.contact,name='contact'),
    url(r'^friends$',footerpages.friendsIknow,name='friends'),
    
    url(r'^copyright$',footerpages.copyright,name='copyright')
]
