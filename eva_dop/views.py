from django.shortcuts import render
from .models import Topic

from django.http import HttpResponseRedirect #редирект
from django.core.urlresolvers import reverse #строит юрл по шаблону

from .forms import TopicForm

# Create your views here.
def index(request):
	#представление главной страницы приложения eva_dop
	return render(request, 'eva_dop/index.html')

def topics(request):
	#делаем вывод тем
	topics = Topic.objects.order_by('date_added')
	context = {'topics': topics}
	return render(request, 'eva_dop/topics.html', context)
	
def topic(request, topic_id):
	#тут запиливаем отдельный вывод треда
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic': topic, 'entries': entries}
	return render(request, 'eva_dop/topic.html', context)
	
def new_topic(request):
	#запиливаем тред
	if request.method != 'POST':
		#нет данных? пустая форма
		form = TopicForm()
	else:
		#отправляем ПОСТ и обрабатываем
		form = TopicForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('eva_dop:topics'))
			
			
	context = {'form': form}
	return render(request, 'eva_dop/new_topic.html', context)
	
def clans(request):
	#представление страницы clans
	return render(request, 'eva_dop/clans.html')
	
def codex(request):
	#представление страницы codex
	return render(request, 'eva_dop/codex.html')
	
def members(request):
	#представление страницы members
	return render(request, 'eva_dop/members.html')
	
def guide(request):
	#представление страницы guide
	return render(request, 'eva_dop/guide.html')