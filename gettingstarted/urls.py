from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("index2", hello.views.index2, name="index2"),
    path("home", hello.views.home, name="home"),
    path("home2", hello.views.home2, name="home2"),
    path("chatbot", hello.views.chatbot, name="chatbot"),
    path("chatbotRespuesta", hello.views.chatbotRespuesta, name="chatbot"),
    path("chatbot2", hello.views.chatbot2, name="chatbot2"),
    path("chatbot2Respuesta", hello.views.chatbot2Respuesta, name="chatbot2"),
    path("chatbotCovid", hello.views.chatbotCovid, name="chatbotCovid"),
    path("chatbotCovidRespuesta", hello.views.chatbotCovidRespuesta, name="chatbotCovid"),
    path("consulta", hello.views.consulta, name="consulta"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
]
