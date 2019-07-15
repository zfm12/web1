from django.contrib import admin
from syy_topics.models import SYY_Topic,SYY_Entry,SYY_Comment

admin.site.register(SYY_Topic)
admin.site.register(SYY_Entry)
admin.site.register(SYY_Comment)
# Register your models here.

admin.site.site_title = "SYY网站"
admin.site.site_header = "SYY网站后台管理"