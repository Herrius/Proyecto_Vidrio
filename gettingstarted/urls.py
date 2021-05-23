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
    path("home", hello.views.index2, name="home"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
]
