from django.urls import path
from .views import *

urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('article/<int:pk>/', ArticlePage.as_view(), name='article_page'),
    path('FeedBack', FeedBackPage.as_view(), name='feedback_page'),
]
