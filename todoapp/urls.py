from django.conf.urls import url
from . import views

## First argument url(r'^$' - URL pattern
## Second argument 'views.signup'- funciton to run
## Third argument 'name = "signup"'- alias 

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^signup', views.signup, name="signup"),
    url(r'^login', views.login, name="login"),
    url(r'^logout', views.logout, name="logout"),
    url(r'^(?P<todo_id>[0-9]+)/done/$', views.done, name='done'),
    url(r'^(?P<todo_id>[0-9]+)/delete/$', views.delete, name='delete'),
]
