from django.db import models
from django.contrib.auth.models import User


class file_information(models.Model):
    id = models.AutoField(primary_key=True)
    file_name = models.CharField(verbose_name="文件名称", max_length=526)
    file_info = models.TextField(verbose_name="文件备注")
    file_create_time = models.DateTimeField(auto_now_add=True, verbose_name="文件创建时间")
    file_change_time = models.DateTimeField(auto_now=True, verbose_name="文件修改时间")
    file = models.FileField(upload_to="static/work/doc/", verbose_name="文件")
    # 文件处理状态  # 1：进行中   0：已完成   2：删除
    file_status = models.IntegerField(default=1, verbose_name="当前状态")
    over_time = models.CharField(default="", max_length=255, verbose_name="截至时间")
    # html_path = models.CharField(default="", max_length=256, verbose_name="html文件")
    word_path = models.CharField(default="", max_length=256, verbose_name="导出word文件")
    # 翻译种类 1：百度翻译       2：搜狗翻译
    fanyi_zl = models.IntegerField(default=0, verbose_name="翻译种类")
    # 翻译种类 1：中文翻译       2：英文翻译
    # fanyi_fx = models.IntegerField(default=0, verbose_name="翻译方向")
    # 1 中译英 2 英译中 0 未设置
    yuan = models.IntegerField(default=0, verbose_name="源文语言种类")
    # 2 中译英 1 英译中 0 未设置
    mubiao = models.IntegerField(default=0, verbose_name="目标语言种类")
    # 文章总字数
    all_num = models.IntegerField(default=0, verbose_name="文章总字数")
    # 当前已修改的字数
    numing = models.IntegerField(default=0, verbose_name="已修改的字数")
    # 文章总段数
    all_para = models.IntegerField(default=0, verbose_name="文章总段数")
    # 当前已修改的段落数
    paraing = models.IntegerField(default=0, verbose_name="已修改段数")
    # 当前进度 保留整数
    jindu = models.IntegerField(default=0, verbose_name="当前的进度")
    # 关联用户
    file_user = models.ForeignKey(User, models.CASCADE)


class yuanwen(models.Model):
    id = models.AutoField(primary_key=True)
    yuanwen = models.TextField(verbose_name="原文句子")
    yuanwen_change = models.TextField(verbose_name="原文修改句子", default="")
    yuanwen_style = models.CharField(max_length=256, verbose_name="原文标题样式", default="")
    style_value = models.CharField(max_length=255, verbose_name="样式的值", default="")
    # 是否修改过 默认0 未修改过  1 修改过  不可再次修改
    check_changeed = models.IntegerField(default=0, verbose_name="是否修改过")
    # gl = models.OneToOneField('self', null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)
    file = models.ForeignKey(file_information, models.CASCADE)


class yiwen(models.Model):
    id = models.AutoField(primary_key=True)
    yiwen = models.TextField(verbose_name="译文句子")
    yiwen_change = models.TextField(verbose_name="译文修改句子", default=" ")
    yiwen_wait_over = models.TextField(verbose_name="译文待人工编译", default="")
    yiwen_style = models.CharField(max_length=256, verbose_name="译文标题样式", default="")
    style_value = models.CharField(max_length=255, verbose_name="样式的值", default="")
    gl = models.OneToOneField(yuanwen, on_delete=models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)
    file = models.ForeignKey(file_information, models.CASCADE)

