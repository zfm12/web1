from django.db import models


class Person(models.Model):
	name = models.CharField(max_length=30)
	position=models.CharField(max_length=30)
	telephone = models.CharField(max_length=20,null=True)
	Landline=models.CharField(max_length=20,null=True)
	class Meta:
		verbose_name_plural='通讯录'
	def __str__(self):
		return self.name
