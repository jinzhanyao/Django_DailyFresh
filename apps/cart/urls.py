from django.conf.urls import url
from django.urls import path

from apps.cart.views import CartAddView, CartInfoView, CartUpdateView, CartDeleteView


app_name = 'cart'
urlpatterns = [
    url(r'^add$', CartAddView.as_view(), name='add'), # 购物车记录添加
    url(r'^$', CartInfoView.as_view(), name='show'), # 购物车页面显示
    url(r'^update$', CartUpdateView.as_view(), name='update'), # 购物车记录更新
    # url(r'^delete$', CartDeleteView.as_view(), name='delete'), # 购物车记录删除
    path('delete', CartDeleteView.as_view(), name='delete'), # 购物车记录删除
]
