from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^file_update/$', views.file_update, name='file_update'),
    url(r'^update/$', views.update, name='update'),
    url(r'^file_info/$', views.file_info, name='file_info'),
    url(r'^trans_type/$', views.trans_type, name='trans_type'),
    # url(r'^(\d+)/(\d+)/(\d+)/work_wait/$', views.work_wait, name='work_wait'),
    url(r'^work_wait/$', views.work_wait, name='work_wait'),
    # 工作区
    # 中文编译界面
    url(r'^(\d+)/work/$', views.work, name='work'),
    # 英文编译界面
    url(r'^(\d+)/enwork/$', views.enwork, name='enwork'),
    # 下载/导出  word
    url(r'^(\d+)/downloads/$', views.downloads, name='downloads'),
    # 删除文档项目
    url(r'^(\d+)/del_file/$', views.del_file, name='del_file'),
    # 单行/全部修改译文
    url(r'^(\d+)/([\s\S]*)/change_yiwen/$', views.change_yiwen, name='change_yiwen'),
    # url(r'^(\d+)/enchange_yiwen/$', views.enchange_yiwen, name='enchange_yiwen'),
    # 生成word
    # url(r'^(\d+)/word_ok/$', views.word_ok, name='word_ok'),
    # 搜索原文
    url(r'serch_yuanwen/(\d+)/$', views.serch_yuanwen, name="serch_yuanwen"),
    url(r'serch_yiwen/(\d+)/$', views.serch_yiwen, name="serch_yiwen"),
    # 中文
    url(r'bdjson/([\s\S]*)/(\d+)/$', views.bdjson, name="bdjson"),
    url(r'sgjson/([\s\S]*)/(\d+)/$', views.sgjson, name="sgjson"),
    # 英文
    url(r'en_baidu/([\s\S]*)/(\d+)/$', views.en_baidu, name="en_baidu"),
    url(r'ensgjson/([\s\S]*)/(\d+)/$', views.ensgjson, name="ensgjson"),
    # url(r'all_change_yiwen/(\d+)/([\s\S]*)/$', views.all_change_yiwen, name="all_change_yiwen"),
    url(r'all_save_yiwen/(\d+)/([\s\S]*)/$', views.all_save_yiwen, name="all_save_yiwen"),
    url(r'change_befor/(\d+)/$', views.change_befor, name="change_befor"),
    url(r'change_old/(\d+)/$', views.change_old, name="change_old"),
    url(r'change_content/([\s\S]*)/(\d+)/$', views.change_content, name="change_content"),
    url(r'en_content_change/([\s\S]*)/(\d+)/$', views.en_content_change, name="en_content_change"),
    url(r'yuanwen_check/(\d+)/$', views.yuanwen_check, name="yuanwen_check"),
    url(r'yiwen_check/(\d+)/$', views.yiwen_check, name="yiwen_check"),
    # 中文编译
    url(r'zh_rs/(\d+)/$', views.zh_rs, name="zh_rs"),
    url(r'en_read_save/(\d+)/$', views.en_read_save, name="en_read_save"),
]