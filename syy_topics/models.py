from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class SYY_Topic(models.Model):
    text=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
	
    class Meta:
        verbose_name_plural='话题'
		
    def __str__(self):
	    #返回模型的字符串表示
        return self.text

class SYY_Entry(models.Model):
    topic=models.ForeignKey(SYY_Topic,on_delete=models.CASCADE)
    text=RichTextField('文章标题')
    date_added=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
	
    class Meta:
	    verbose_name_plural='回答'
		
    def __str__(self):
	    return self.text[:30]+"..."
	
class SYY_Comment(models.Model):
    target=models.ForeignKey(SYY_Entry,on_delete=models.CASCADE)
    content=models.CharField(max_length=2000,verbose_name="内容")
    nicknam=models.ForeignKey(User,on_delete=models.CASCADE)
    created_time=models.DateTimeField(auto_now_add=True)
	
    class Meta:
	    verbose_name=verbose_name_plural="评论"
		
    def __str__(self):
	    #返回模型的字符串表示
        return self.content