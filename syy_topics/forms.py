from django import forms
from .models import SYY_Topic,SYY_Entry,SYY_Comment
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class TopicForm(forms.ModelForm):
	class Meta:
		model=SYY_Topic
		fields=['text']
		labels={'text': ''}
		
class EntryForm(forms.ModelForm):
	class Meta:
		model =SYY_Entry
		fields = ['text']
		labels = {'text': ''}
		#widgets = {'owner': forms.CharField}                
		#widgets = {'text': forms.Textarea(attrs={'cols': 80})} 
		#widgets = {'text': forms.CharField(widget=CKEditorWidget(),label='正文',required=True)} 
		text=forms.CharField(widget=CKEditorUploadingWidget(),label='正文',required=False)
		#text=RichTextField()
class CommentForm(forms.ModelForm):
	class Meta:
		model=SYY_Comment
		fields=['content']
		labels = {'content': ''}
		#content = forms.CharField(widget=forms.TextInput(attrs={'size': '1000'}))
		widgets = {'content': forms.Textarea(attrs={'rows': 1})} 