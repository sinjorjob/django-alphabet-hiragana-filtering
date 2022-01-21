from django.urls import path
from . import views


urlpatterns = [

   path('list/', views.BookListView.as_view(), name='index'),
   path('list/<str:q>', views.BookFilterView.as_view(), name='filter'),
]

