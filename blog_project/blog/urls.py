from django.urls import path
from blog import views
urlpatterns = [
    path('bloglist/',views.blog_list,name='bloglist'),
    path('generic/blogs/', views.GenericBlogList.as_view()),
    path('generic/blog/<int:pk>', views.GenericBlogDetail.as_view()),
    path('api/blogs/',views.blog_list_api),
    path('api/blogs/<int:blog_id>', views.blog_detail_api),
    path('category/',views.category_list,name='categorylist'),
    path('comment/', views.write_comment, name='writecomment'),
    path('comment/approve/<int:comment_id>', views.approve_comment, name='approvecomment'),
    path('comment/remove/<int:comment_id>', views.remove_comment, name='removecomment'),
    path('topic/<int:topic_id>', views.topic_list, name='topic'),
    path('category/<int:category_id>', views.category_detail, name='categorydetail'),
    path('blog/<int:blog_id>',views.blog_detail,name='blogdetail'),
    path('add_blog/',views.add_new_blog,name='add_blog'),

]
