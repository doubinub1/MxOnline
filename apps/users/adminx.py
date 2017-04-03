# _*_ coding: utf-8 _*_

__author__ = 'pluto'
__date__ = '2017/4/3 下午9:10'


import xadmin


from .models import EmailVerifyRecord
from .models import Banner

class EmailVerifyRecordAdmin(object):
    list_display = ['id','code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email']
    list_filter = ['id','code', 'email', 'send_type', 'send_time']

class BannerAdmin(object):
    list_display = ['id','title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['id','title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)
