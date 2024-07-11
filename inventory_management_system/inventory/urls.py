from django.conf.urls import  url
from .views import *

urlpatterns = [

    url(r'^$', index, name='index'),
    url(r'^laptops$', display_laptops, name="display_laptops"),
    url(r'^desktops$', display_desktops, name="display_desktops"),
    url(r'^mobiles$', display_mobiles, name="display_mobiles"),
    url(r'^printers$', display_printers, name="display_printers"),
    url(r'^routers$', display_routers, name="display_routers"),
    url(r'^toughpad$', display_toughpad, name="display_toughpad"),
    url(r'^toughbook$', display_toughbook, name="display_toughbook"),

    url(r'^add_laptop$', add_laptop, name="add_laptop"),
    url(r'^add_desktop$', add_desktop, name="add_desktop"),
    url(r'^add_mobile$', add_mobile, name="add_mobile"),
    url(r'^add_printer$', add_printers, name="add_printer"),
    url(r'^add_router$', add_routers, name="add_router"),
    url(r'^add_toughpad$', add_toughpad, name="add_toughpad"),
    url(r'^add_toughbook$', add_toughbook, name="add_toughbook"),

    url(r'^laptops/edit_item/(?P<pk>\d+)$', edit_laptop, name="edit_laptop"),
    url(r'^desktops/edit_item/(?P<pk>\d+)$', edit_desktop, name="edit_desktop"),
    url(r'^mobiles/edit_item/(?P<pk>\d+)$', edit_mobile, name="edit_mobile"),
    url(r'^printers/edit_item/(?P<pk>\d+)$', edit_printers, name="edit_printers"),
    url(r'^routers/edit_item/(?P<pk>\d+)$', edit_routers, name="edit_routers"),
    url(r'^toughpad/edit_item/(?P<pk>\d+)$', edit_toughpad, name="edit_toughpad"),
    url(r'^toughbook/edit_item/(?P<pk>\d+)$', edit_toughbook, name="edit_toughbook"),

    url(r'^laptops/delete/(?P<pk>\d+)$', delete_laptop, name="delete_laptop"),
    url(r'^desktops/delete/(?P<pk>\d+)$', delete_desktop, name="delete_desktop"),
    url(r'^mobiles/delete/(?P<pk>\d+)$', delete_mobile, name="delete_mobile"),
    url(r'^printers/delete/(?P<pk>\d+)$', delete_printers, name="delete_printer"),
    url(r'^routers/delete/(?P<pk>\d+)$', delete_routers, name="delete_router"),
    url(r'^toughpad/delete/(?P<pk>\d+)$', delete_toughpad, name="delete_toughpad"),
    url(r'^toughbook/delete/(?P<pk>\d+)$', delete_toughbook, name="delete_toughbook"),

]
