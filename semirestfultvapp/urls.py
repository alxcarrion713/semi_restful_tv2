from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", views.index),
    path("shows", views.shows),
    path("shows/new", views.addshow),
    path("shows/create", views.createshow),
    path("shows/<idshow>", views.showinfo),
    path("shows/<idshow>/edit", views.editshow),
    path("shows/<idshow>/update", views.updateshow),
    path("shows/<idshow>/destroy", views.delete)
]
