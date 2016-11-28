#from blog.views import post_list
#
#urlpatterns = patterns('qa.views',
 #   url(r'^login/','test'),
#)

from django.conf.urls import url


from . import views

from qa.views import test

urlpatterns = [
    url(r'^login/', test, name='test'),
]
