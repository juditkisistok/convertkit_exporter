from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login-page'),
    path('logout/', views.logoutUser, name='logout-page'),
    path('register/', views.registerUser, name='register-page'),

    path('tags/', views.display_tags, name='display_tags'),
    path('', views.display_tags, name='display_tags'),
    path('download/<int:tag>_<str:name>', views.download_tag_subs, name='download'),
    path('download-all/', views.download_all_subs, name='download-all'),
    path('api/', views.inputAPI, name='inputAPI'),
    path('update-api/<str:email>', views.updateAPI, name='updateAPI'),
    path('delete-api/<str:email>', views.deleteAPI, name='deleteAPI'),

]