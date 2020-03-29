from django.db import models
from apps.goods.models import GoodsSKU
from db.base_model import BaseModel


class GoodsSKUIndex(BaseModel):
    # 索引字段 use_template=True指定根据表中的哪些字段建立索引文件的说明放在一个文件中
    # text = indexes.CharField(document=True, use_template=True)
    text = models.CharField(document=True, use_template=True, db_index=True)
    def get_model(self):
        # 返回你的模型类
        return GoodsSKU

    # 建立索引的数据
    def index_queryset(self, using=None):
        return self.get_model().objects.all()
