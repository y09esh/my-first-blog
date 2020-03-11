from django.urls import path
from . import views
app_name='blog'

urlpatterns= [
    # post views
    #path('',views.post_list,name='post_list'),
    path('',views.PostListView.as_view(),name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name = 'post_detail'),
    #path('post/new/',views.post_new, name='post_new'),
    #path('post/<int:pk>/edit/', views.post_edit, name = 'post_edit'),
    ]
