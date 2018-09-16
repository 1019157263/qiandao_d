from django.contrib import admin

# Register your models here.



from .models import user,data,log_a


class log_aAdmin(admin.ModelAdmin):
    list_filter = ['time']#过滤器
    search_fields = ['username']
    list_display = ('name','username','time')

class userAdmin(admin.ModelAdmin):
    list_filter = ['time']#过滤器
    search_fields = ['username']
    list_display = ('username','time')
    fieldsets = [
        ('RMB余额:',               {'fields': ['rmb']}),
         ('剩余签到应用数:',               {'fields': ['yingyong']}),
        ('用户名', {'fields': ['username']}),
          ('密码:',               {'fields': ['pwd'], 'classes': ['collapse']}),
            ('邮箱:',               {'fields': ['email']}),
             ('注册时间:',               {'fields': ['time'], 'classes': ['collapse']}),
            
        
    ]#显示顺序




admin.site.register(user,userAdmin)

admin.site.register(data)
admin.site.register(log_a,log_aAdmin)
