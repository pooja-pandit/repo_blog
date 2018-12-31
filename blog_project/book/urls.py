from django.urls import path
from book import views
urlpatterns = [
    path('publishers/',views.PublisherList.as_view(),name='PublisherList'),
    path('books/', views.BookList.as_view(), name='BookList'),
    path('publisher/<int:pk>/', views.PublisherDetail.as_view(), name='PublisherDetail'),

]