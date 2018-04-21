from django.conf.urls import url

from . import views

urlpatterns = [
	#Заглавная страница
	url(r'^$', views.index, name='index'),
	#выводим все созданные темы
	url(r'^topics/$', views.topics, name='topics'),
	#запиливаем отдельные юрл для каких-то тем, в данном случае для созданных записек/тем
	url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
	#перенаправление на страницу запиливания треда
	url(r'^new_topic/$', views.new_topic, name='new_topic'),
	
	#тут идёт пачка "основных" страниц
	url(r'^clans/$', views.clans, name='clans'),
	url(r'^codex/$', views.codex, name='codex'),
	url(r'^members/$', views.members, name='members'),
	url(r'^guide/$', views.guide, name='guide'),
]