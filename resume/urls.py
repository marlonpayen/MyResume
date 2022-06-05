'''
Created on 3 May 2022

@author: mpayen
'''
from django.urls import path
from resume import views
# import settings and static first
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
