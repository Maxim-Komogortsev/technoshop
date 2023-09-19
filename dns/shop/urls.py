from . import views
from django.urls import path, re_path

urlpatterns = [
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
         views.product_info,
         name='product_info'),
    re_path(r'^$', views.show_product_list, name='show_product_list'),
    re_path(r'^(?P<category_slug>[-\w]+)/$',
         views.show_product_list,
         name='show_product_list_by_category'),
]