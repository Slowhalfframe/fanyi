from django.db import models
# 导入内置的用户表
from django.contrib.auth.models import User


# 创建用户的扩展信息表
class users_more_info(models.Model):
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=11, null=True, verbose_name='手机号码')
    # 绑定
    user = models.OneToOneField(User, on_delete=models.CASCADE)
