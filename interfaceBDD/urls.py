from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^accueil', views.home),
    url(r'^addProp/', views.proposition, name = 'prop'),
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', views.addition),
    url(r'^testsoumis/$', views.validation)
]