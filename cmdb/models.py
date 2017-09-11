from django.db import models

# Create your models here.

#创建两字段保存用户名字和密码
class UserInfo(models.Model):
	user = models.CharField(max_length=32)
	pwd = models.CharField(max_length=32)
