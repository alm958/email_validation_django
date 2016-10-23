from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index' ),
    # url(r'^login$', views.login, name='login' ),
    url(r'^register$', views.register, name='register' ),
    # url(r'^logout$', views.logout, name='logout' ),
    url(r'^show_emails$', views.show_emails, name='show_emails' ),
    # url(r'^edituser/(?P<id>d+)$', views.edituser, name='edituser' ),
    # url(r'^updateuser/(?P<id>d+)$', views.updateuser, name='updateuser' ),
    # url(r'^deleteemail/(?P<id>d+)$', views.deleteemail, name='deleteemail' ),
    # url(r'^wall$', views.wall, name='wall' ),
    # url(r'^newmessage$', views.newmessage, name='newmessage' ),
    # url(r'^editmessage/(?P<id>d+)$', views.editmessage, name='editmessage' ),
    # url(r'^delmessage/(?P<id>d+)$', views.delmessage, name='delmessage' ),
    # url(r'^newcomment$', views.newcomment, name='newcomment' ),
    # url(r'^editcomment/(?P<id>d+)$', views.editcomment, name='editcomment' ),
    # url(r'^delcomment/(?P<id>d+)$', views.delcomment, name='delcomment' ),
    url(r'^del_email/(?P<id>\d+)$', views.del_email, name='del_email' ),
    url(r'^del_prompt/(?P<id>\d+)$', views.del_prompt, name='del_prompt' ),
]
