from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_tags, name='display_tags'),
    path('download/<int:tag>', views.download_tag_subs, name='download'),
    path('api/', views.inputAPI, name='inputAPI'),
    path('update-api/<str:email>', views.updateAPI, name='updateAPI'),
    path('delete-api/<str:email>', views.deleteAPI, name='deleteAPI'),

]