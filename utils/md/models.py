from django.db import models


class ModelBase(models.Model):
    """
    公用字段,用于其他表继承
    """
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")  # 创建时间 日期
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")  # 修改时间
    is_delete = models.BooleanField(default=False, verbose_name="逻辑删除")  # 删除标识

    class Meta:
        # 为抽象模型类,用于其他模型继承,数据库迁移时不会创建
        abstract = True
