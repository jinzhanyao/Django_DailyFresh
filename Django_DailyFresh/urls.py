from django.apps import apps
from django.contrib import admin
from django.urls import path, include

from apps.goods.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')), # 富文本编辑器
    # path('search/', include('haystack.urls')), # 全文检索框架
    path('cart/', include('apps.cart.urls')),
    path('goods/', include('apps.goods.urls')),
    path('order/', include('apps.order.urls')),
    path('user/', include('apps.user.urls')),
    path('', IndexView.as_view(), name='index'), # 首页
]
