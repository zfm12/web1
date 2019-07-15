from django.shortcuts import render
from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse
from django.urls import reverse
from .models import SYY_Topic,SYY_Entry
from .forms import TopicForm,EntryForm,CommentForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.shortcuts import render, get_object_or_404,render_to_response


def index(request):
	return render(request,'syy_topics/index.html')
# Create your views here.

@login_required
def topics(request):       #显示所有的话题，并在话题前面增加查询的界面
	if 'q' in request.GET:   #如果有请求
		q = request.GET['q']   #获取请求的数据
		if not q:              #如果请求的数据是空白
			topics=SYY_Topic.objects.order_by('date_added')
			#topics=SYY_Topic.objects.filter(owner=request.user).order_by('date_added') 
			#上面这句将界面变成了用户只能显示属于自己的话题
			context={'topics':topics}
			return render(request,'syy_topics/topics.html',context)
		else:
			topics = SYY_Topic.objects.filter(text__contains=q)
			context1={'topics':topics}
			return render(request,'syy_topics/topics.html',context1)
	else:
		topics=SYY_Topic.objects.order_by('date_added')
		#topics=SYY_Topic.objects.filter(owner=request.user).order_by('date_added') 
		#上面这句将界面变成了用户只能显示属于自己的话题
		context={'topics':topics}
		return render(request,'syy_topics/topics.html',context)
		
@login_required  
def topic(request,topic_id):   #显示特定主体的详细页面
	#topic=SYY_Topic.objects.get(id=topic_id)  #当topic_id=2的时候，topic=测试
	topic = get_object_or_404(SYY_Topic, id=topic_id)
	entries = topic.syy_entry_set.order_by('-date_added') 
	'''number=[]
	b=len(entries)
	for entry in entries:
		a=len(entry.syy_comment_set.order_by('-created_time'))
		number.append(a)'''
	context={'topic':topic,'entries':entries}
	return render(request,'syy_topics/topic.html',context)
	

@login_required
def new_topic(request):   #添加新的话题
	if request.method != 'POST':
		form = TopicForm()
	else:
		form = TopicForm(request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
			return HttpResponseRedirect(reverse('syy_topics:topics'))
	context = {'form': form}
	return render(request, 'syy_topics/new_topic.html', context)

@login_required	
def new_entry(request, topic_id): #增加一个内容在特定的主题下
    topic = SYY_Topic.objects.get(id=topic_id)
    #if topic.owner != request.user:
        #raise Http404
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()        
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.owner = request.user
            new_entry.save()
            return HttpResponseRedirect(reverse('syy_topics:topic',
                                        args=[topic_id]))
    
    context = {'topic': topic, 'form': form}
    return render(request, 'syy_topics/new_entry.html', context)

@login_required	
def edit_entry(request,entry_id):  #编辑条目
	entry=SYY_Entry.objects.get(id=entry_id)
	topic=entry.topic
	if entry.owner !=request.user:  #只有作者本人才可编辑,将topic.owner换成了entry.owner
		#raise Http404
		return HttpResponse("您不能编辑其他人的答案",status=404)
	if request.method !='POST':
		form=EntryForm(instance=entry)
	else:
		form=EntryForm(instance=entry,data=request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('syy_topics:topic',args=[topic.id]))
	context={'entry':entry,'topic':topic,'form':form}
	return render(request,'syy_topics/edit_entry.html',context)
	
def entry(request,entry_id):   #显示特定主体的详细页面
	entry=SYY_Entry.objects.get(id=entry_id)
	comments = entry.syy_comment_set.order_by('-created_time')
	context={'entry':entry,'comments':comments}
	return render(request,'syy_topics/entry.html',context)
	
	
def new_comment(request,entry_id):
	entry = SYY_Entry.objects.get(id=entry_id)
	if request.method != 'POST':
		# 没有数据提交创建一个新的表格.
		form = CommentForm()        
	else:
		#POST data submitted; process data.
		form = CommentForm(data=request.POST)
		if form.is_valid():
			new_comment = form.save(commit=False)
			new_comment.target = entry
			new_comment.nicknam = request.user
			new_comment.save()
			return HttpResponseRedirect(reverse('syy_topics:entry',args=[entry_id]))
    
	context = {'entry': entry, 'form': form}
	return render(request, 'syy_topics/new_comment.html', context)
	
def owner(request):	
	entries = SYY_Entry.objects.filter(owner=request.user).order_by('date_added') 		
	context={'entries':entries}
	return render(request,'syy_topics/owner.html',context)
