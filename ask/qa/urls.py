urlpatterns =  patterns('qa.views',
  url(r'^$', 'test', name = 'root'),
  url(r'^login/', 'test'),
  url(r'^signup/', 'test', name = 'signup'),
  url(r'^question/\w+/', 'test', name = 'question'),
  url(r'^ask/', 'test', name = 'ask'),
  url(r'^popular/', 'test', name = 'popular'),
  url(r'^new/', 'test', name = 'new'),
)
