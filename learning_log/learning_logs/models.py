from django.db import models
# Create your models here.


class Topic(models.Model):
    # 用户学习的主题，继承Model，它定义了模型的基本功能
    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)  # 设置当前日期时间

    def __str__(self):  # 模型的字符串表示
        return self.text