from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

from utils.md.models import ModelBase


class Bureau(ModelBase):
    """
    地市局信息表
    """
    bureau_name = models.CharField(max_length=10, verbose_name="地市局名", help_text="地市局名")

    class Meta:
        db_table = "tb_bureau"  # 指明数据库表名
        verbose_name = "地市局信息表"
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        return "<{}>".format(self.bureau_name)


class ParentDepartment(ModelBase):
    """
    上级部门信息表
    """
    parent_name = models.CharField(max_length=20, verbose_name="上级部门", help_text="上级部门")
    own_bureau = models.ForeignKey('Bureau', on_delete=models.DO_NOTHING, null=True)

    class Meta:
        db_table = "tb_ParentDep"  # 指明数据库表名
        verbose_name = "地市局信息表"
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        return "<{}\t{}>".format(self.own_bureau.bureau_name, self.parent_name)


class Department(ModelBase):
    """
    部门信息表
    """
    dep_name = models.CharField(max_length=20, verbose_name="部门", help_text="部门")

    class Meta:
        db_table = "tb_Dep"  # 指明数据库表名
        verbose_name = "部门信息表"
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        return "<{}>".format(self.dep_name)


class Users(AbstractUser):
    """
    用户模型
    """
    parent_name = models.ForeignKey('ParentDepartment', on_delete=models.DO_NOTHING, blank=True)
    dep_name = models.ForeignKey('Department', on_delete=models.DO_NOTHING, blank=True)
    job = models.CharField(max_length=20, help_text='职务', verbose_name='职务', blank=True)
    others = models.CharField(max_length=40, help_text='备注', verbose_name='备注', blank=True)
    mobile = models.CharField(  # 手机号字段
        max_length=11,
        # unique=True,
        help_text="手机号",
        verbose_name="手机号",
        error_messages={
            'unique': "此手机号已经注册"
            , }, )
    objects = UserManager()

    class Meta:
        db_table = "tb_Users"
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def get_groups_name(self):
        groups_name_list = [i.name for i in self.groups.all()]
        return ' | '.join(groups_name_list)

    def __str__(self):
        return self.username
