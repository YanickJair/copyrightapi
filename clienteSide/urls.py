from django.conf.urls import url
from clienteSide import views

urlpatterns = [
    url(r'^area-aplicacao/$', views.AreaAplicacaoList.as_view(), name='area-aplicacao'),
    url(r'^area-aplicacao/(?P<pk>[0-9]+)/$', views.AreaAplicacaoDetail.as_view(), name='area-aplicacao'),
    
    url(r'^tipo-obra/$', views.TipoObraList.as_view(), name='tipo-obra'),
    url(r'^tipo-obra/(?P<pk>[0-9]+)/$', views.TipoObraDetail.as_view(), name='tipo-obra'),
    
    url(r'^licenca/$', views.LicencaList.as_view(), name='licenca'),
    url(r'^licenca/(?P<pk>[0-9]+)/$', views.LicencaDetail.as_view(), name='licenca'),
    
    url(r'^tipo-perfil/$', views.TipoPerfilList.as_view(), name='tipo-perfil'),
    url(r'^tipo-perfil/(?P<pk>[0-9]+)/$', views.TipoPerfilDetail.as_view(), name='tipo-perfil'),

    url(r'^commentary/$', views.CommentaryList.as_view(), name='commentary'),
    url(r'^commentary/(?P<pk>[0-9]+)/$', views.CommentaryDetail.as_view(), name='commentary'),

    url(r'^commentary-reply/$', views.CommentaryReplyList.as_view(), name='commentary-reply'),
    url(r'^commentary-reply/(?P<pk>[0-9]+)/$', views.CommentaryReplyDetail.as_view(), name='commentary-reply'),

    url(r'^obra/$', views.ObraList.as_view(), name='obra'),
    url(r'^obra/(?P<pk>[0-9]+)/$', views.ObraDetail.as_view(), name='obra'),

    url(r'^create-account/$', views.UserList.as_view(), name='create-account'),
    url(r'^create-account/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='create-account')
]