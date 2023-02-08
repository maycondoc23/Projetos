from django.urls import path, include
from . import views
from .views import passwordchangeview, usuariocreate,ict1statuse14, ict1statusideapad1, ict1statusideapad3a, ict1statusideapad3i, ict1statusm75, ict1statusneo,ict2statusideapad1,ict2statuse14, PaginaInicial, n50schart, home, ict2statusneo, ict2statusm75, m75chart,ideapad1chart,ideapad3achart,ideapad3ichart,e14chart, ict2statusideapad3i
#import del
from .views import ideapad1ict1del, ideapad3aict1del, ideapad3iict1del, m75ict1del, n50sict1del
from .views import ideapad1ict2del, ideapad3aict2del, ideapad3iict2del, m75ict2del, n50sict2del
from .views import ideapad1ict3del, ideapad3aict3del, ideapad3iict3del, m75ict3del, n50sict3del
#import list
from .views import n50sict1list, m75ict1list, ideapad1ict1list, ideapad3aict1list, ideapad3iict1list, e14ict1list
from .views import n50sict2list, m75ict2list, ideapad1ict2list, ideapad3aict2list, ideapad3iict2list, e14ict2list
from .views import n50sict3list, m75ict3list, ideapad1ict3list, ideapad3aict3list, ideapad3iict3list, e14ict3list

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
    path('usuariocreate', views.usuariocreate.as_view(), name='usuariocreate'),
    path('usuarioedit', passwordchangeview.as_view(), name='usuarioedit'),


   ### LIST VIEWS ###
#ict1 
    path('n50sict1list', views.n50sict1list.as_view(), name='n50sict1list'),
    path('m75ict1list', views.m75ict1list.as_view(), name='m75ict1list'),
    path('ideapad1ict1list', views.ideapad1ict1list.as_view(), name='ideapad1ict1list'),
    path('ideapad3aict1list', views.ideapad3aict1list.as_view(), name='ideapad3aict1list'),
    path('ideapad3iict1list', views.ideapad3iict1list.as_view(), name='ideapad3iict1list'),
    path('e14ict1list', views.e14ict1list.as_view(), name='e14ict1list'),
   
#ict2
    path('n50sict2list', views.n50sict2list.as_view(), name='n50sict2list'),
    path('m75ict2list', views.m75ict2list.as_view(), name='m75ict2list'),
    path('ideapad1ict2list', views.ideapad1ict2list.as_view(), name='ideapad1ict2list'),
    path('ideapad3aict2list', views.ideapad3aict2list.as_view(), name='ideapad3aict2list'),
    path('ideapad3iict2list', views.ideapad3iict2list.as_view(), name='ideapad3iict2list'),
    path('e14ict2list', views.e14ict2list.as_view(), name='e14ict2list'),

#ict3
    path('n50sict3list', views.n50sict3list.as_view(), name='n50sict3list'),
    path('m75ict3list', views.m75ict3list.as_view(), name='m75ict3list'),
    path('ideapad1ict3list', views.ideapad1ict3list.as_view(), name='ideapad1ict3list'),
    path('ideapad3aict3list', views.ideapad3aict3list.as_view(), name='ideapad3aict3list'),
    path('ideapad3iict3list', views.ideapad3iict3list.as_view(), name='ideapad3iict3list'),
    path('e14ict3list', views.e14ict3list.as_view(), name='e14ict3list'),

   ### DELETE FORMS ###

#ict1
   path('n50sict1del/reg/<int:pk>/', views.n50sict1del.as_view(), name='n50sict1del'),
   path('m75ict1del/reg/<int:pk>/', views.m75ict1del.as_view(), name='m75ict1del'),
   path('ideapad1ict1del/reg/<int:pk>/', views.ideapad1ict1del.as_view(), name='ideapad1ict1del'),
   path('ideapad3iict1del/reg/<int:pk>/', views.ideapad3iict1del.as_view(), name='ideapad3iict1del'),
   path('ideapad3aict1del/reg/<int:pk>/', views.ideapad3aict1del.as_view(), name='ideapad3aict1del'),
   path('e14ict1del/reg/<int:pk>/', views.e14ict1del.as_view(), name='e14ict1del'),
#ict2
   path('n50sict2del/reg/<int:pk>/', views.n50sict2del.as_view(), name='n50sict2del'),
   path('m75ict2del/reg/<int:pk>/', views.m75ict2del.as_view(), name='m75ict2del'),
   path('ideapad1ict2del/reg/<int:pk>/', views.ideapad1ict2del.as_view(), name='ideapad1ict2del'),
   path('ideapad3iict2del/reg/<int:pk>/', views.ideapad3iict2del.as_view(), name='ideapad3iict2del'),
   path('ideapad3aict2del/reg/<int:pk>/', views.ideapad3aict2del.as_view(), name='ideapad3aict2del'),
   path('e14ict2del/reg/<int:pk>/', views.e14ict2del.as_view(), name='e14ict2del'),
#ict3
   path('n50sict3del/reg/<int:pk>/', views.n50sict3del.as_view(), name='n50sict3del'),
   path('m75ict3del/reg/<int:pk>/', views.m75ict3del.as_view(), name='m75ict3del'),
   path('ideapad1ict3del/reg/<int:pk>/', views.ideapad1ict3del.as_view(), name='ideapad1ict3del'),
   path('ideapad3iict3del/reg/<int:pk>/', views.ideapad3iict3del.as_view(), name='ideapad3iict3del'),
   path('ideapad3aict3del/reg/<int:pk>/', views.ideapad3aict3del.as_view(), name='ideapad3aict3del'),
   path('e14ict3del/reg/<int:pk>/', views.e14ict3del.as_view(), name='e14ict3del'),


    ###  INPUT FORMS  ###

#ict1
    path('ict1statusm75', views.ict1statusm75, name='ict1statusm75'),
    path('ict1statusneo', views.ict1statusneo, name='ict1statusneo'),
    path('ict1statusideapad3i', views.ict1statusideapad3i, name='ict1statusideapad3i'),
    path('ict1statusideapad3a', views.ict1statusideapad3a, name='ict1statusideapad3a'),
    path('ict1statuse14', views.ict1statuse14, name='ict1statuse14'),
    path('ict1statusideapad1', views.ict1statusideapad1, name='ict1statusideapad1'),
#ict2
    path('ict2statusm75', views.ict2statusm75, name='ict2statusm75'),
    path('ict2statusneo', views.ict2statusneo, name='ict2statusneo'),
    path('ict2statusideapad3i', views.ict2statusideapad3i, name='ict2statusideapad3i'),
    path('ict2statusideapad3a', views.ict2statusideapad3a, name='ict2statusideapad3a'),
    path('ict2statuse14', views.ict2statuse14, name='ict2statuse14'),
    path('ict2statusideapad1', views.ict2statusideapad1, name='ict2statusideapad1'),
#ict3
    path('ict3statusm75', views.ict3statusm75, name='ict3statusm75'),
    path('ict3statusneo', views.ict3statusneo, name='ict3statusneo'),
    path('ict3statusideapad3i', views.ict3statusideapad3i, name='ict3statusideapad3i'),
    path('ict3statusideapad3a', views.ict3statusideapad3a, name='ict3statusideapad3a'),
    path('ict3statuse14', views.ict3statuse14, name='ict3statuse14'),
    path('ict3statusideapad1', views.ict3statusideapad1, name='ict3statusideapad1'),



   ### graficos ###
    path('n50schart', views.n50schart, name='n50schart'),
    path('m75chart', views.m75chart, name='m75chart'),
    path('e14chart', views.e14chart, name='e14chart'),
    path('ideapad1chart', views.ideapad1chart, name='ideapad1chart'),
    path('ideapad3ichart', views.ideapad3ichart, name='ideapad3ichart'),
    path('ideapad3achart', views.ideapad3achart, name='ideapad3achart'),
    
]
