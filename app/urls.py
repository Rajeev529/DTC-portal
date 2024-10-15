from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.homepage,name="homepage"),
    path("terminal_signup",views.terminal_signup),
    path("register_admin",views.register_admin),
    path("terminal_login",views.terminal_login),
    path("login",views.login), #today
    path("adddriver",views.adddriver),
    path("sendtodriver",views.sendtodriver),
    path("attend",views.attend),
    path("mark_attend",views.mark_attend),
    path("showattend",views.showattend),
    path("driverlogin",views.driverlogin),
    # path("driverhtml",views.driverhtml),
    path("driver_login",views.driver_login),
    # path("chq_attend",views.chq_attend),
    path("driverattend",views.driverattend),
    path("index",views.index),
    path("showdriver",views.showdriver),
    path("updatedata",views.update_data),
    path("delete",views.delete_data),
    path("edit",views.edit_data),
    path("fetchstop",views.fetchstop),
    path("show_data",views.indexshow,name="show_data"),
    path("adminpage",views.admin),
    path("asign",views.asign),
    path("logoutdriver",views.logoutdriver),
]
