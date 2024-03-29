from django.urls import include, path
from rest_framework import routers
from gitinterface import views



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('init/', views.GRPCInitView.as_view()),
    path('add/', views.FileUploadView.as_view()),

    path('repo/', views.RepoView.as_view()),
    path('tree/', views.TreeView.as_view())
]