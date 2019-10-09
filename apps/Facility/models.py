from django.db import models
from utils.md.models import ModelBase
from django.utils import timezone

from user.models import Users


# Create your models here.

class Kind(ModelBase):
    """
    设备名称    台式机，笔记本，...
    """
    kind = models.CharField(max_length=10, verbose_name="设备名称", help_text="设备名称")

    class Meta:
        db_table = "tb_kind"  # 指明数据库表名
        verbose_name = "设备名称"
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        return "<{}>".format(self.kind)


class Brand(ModelBase):
    """
    品牌      华硕，联想....
    """
    brand = models.CharField(max_length=10, verbose_name="品牌", help_text="品牌")
    kind = models.ManyToManyField(Kind, through='KindBrand')

    class Meta:
        db_table = "tb_brand"  # 指明数据库表名
        verbose_name = "品牌"
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        return "<{}>".format(self.brand)


class KindBrand(ModelBase):
    """
    种类 品牌 关系表
    """
    kind = models.ForeignKey(Kind, on_delete=models.DO_NOTHING)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "tb_kind_brand_relationship"  # 指明数据库表名
        verbose_name = "品牌"
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        return "<{}-{}>".format(self.kind, self.brand)


class Type(ModelBase):
    """
    型号   种类-品牌  型号
    """
    unitType = models.CharField(max_length=10, verbose_name="型号", help_text="型号")
    kindBrand = models.ForeignKey(KindBrand, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "tb_type"  # 指明数据库表名
        verbose_name = "型号"
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        return "<{}-{}>".format(self.kindBrand, self.unitType)


class Property(ModelBase):
    """
    产权单位
    """
    prop = models.CharField(max_length=10, verbose_name="产权单位", help_text="产权单位")

    class Meta:
        db_table = "tb_prop"  # 指明数据库表名
        verbose_name = "产权单位"
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        return "<{}>".format(self.prop)


class Supplier(ModelBase):
    """
    供应商
    """
    supplier = models.CharField(max_length=10, verbose_name="供应商", help_text="供应商")

    class Meta:
        db_table = "tb_supplier"  # 指明数据库表名
        verbose_name = "供应商"
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        return "<{}>".format(self.supplier)


class ComeFrom(ModelBase):
    """
    项目来源
    """
    comeFrom = models.CharField(max_length=10, verbose_name="项目来源", help_text="项目来源")

    class Meta:
        db_table = "tb_comeFrom"  # 指明数据库表名
        verbose_name = "项目来源"
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        return "<{}>".format(self.comeFrom)


class Facility(ModelBase):
    """
    设备对象
    """
    unitType = models.ForeignKey(Type, on_delete=models.DO_NOTHING)
    lineNum = models.CharField(max_length=20, verbose_name="条形码编码", help_text="条形码编码", null=True, blank=True)
    serialNum = models.CharField(max_length=20, verbose_name="序列号", help_text="序列号", null=True, blank=True)
    ip = models.CharField(max_length=20, verbose_name="IP地址", help_text="IP地址", null=True, blank=True)
    mac = models.CharField(max_length=48, verbose_name="mac地址", help_text="mac地址", null=True, blank=True)
    onLine = models.BooleanField(default=True, verbose_name="设备状态", help_text="设备状态")
    user = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, blank=True)
    come_time = models.DateTimeField(default=timezone.now, verbose_name="投运时间", help_text="投运时间")
    period = models.IntegerField(default=3, verbose_name="保修年限", help_text="保修年限")
    expiration = models.DateTimeField(default=timezone.now, verbose_name="保修截止日期", help_text="保修截止日期")
    prop = models.ForeignKey(Property, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="产权单位",
                             help_text="产权单位")
    isIt = models.BooleanField(default=True, verbose_name="是否资产", help_text="是否资产")
    oldNum = models.CharField(max_length=20, verbose_name="原资产编码", help_text="原资产编码", null=True, blank=True)
    ItSM = models.CharField(max_length=20, verbose_name="ItSM设备编码", help_text="ItSM设备编码", null=True, blank=True)
    moneyNum = models.CharField(max_length=20, verbose_name="财务资产编码", help_text="财务资产编码", null=True, blank=True)
    oldMoney = models.CharField(max_length=10, verbose_name="资产原值", help_text="资产原值", null=True, blank=True)
    nowMoney = models.CharField(max_length=10, verbose_name="资产现值", help_text="资产现值", null=True, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="供应商",
                                 help_text="供应商")
    comeForm = models.ForeignKey(ComeFrom, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="项目来源",
                                 help_text="项目来源")

# class Pc(ModelBase):
#     """
#     台式机  OnetoOneFiled Github
#     """
#
